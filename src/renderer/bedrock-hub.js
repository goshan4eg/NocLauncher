(() => {
  const $ = (s) => document.querySelector(s);
  let hostWanted = false;

  function setHostStatus(t) {
    const el = $('#hostStatus');
    if (el) el.textContent = t;
  }
  function setInviteStatus(t) {
    const el = $('#inviteStatus');
    if (el) el.textContent = t || '';
  }

  function paintHostToggle() {
    const btn = $('#btnHostToggle');
    if (!btn) return;
    btn.textContent = `Хост: ${hostWanted ? 'ON' : 'OFF'}`;
    btn.classList.toggle('acc', hostWanted);
  }

  async function refresh() {
    const root = $('#servers');
    if (!root) return;

    const r = await window.noc.localServersList();
    if (!r?.ok) {
      root.innerHTML = `<div class="meta">Реестр недоступен (${r?.error || 'unknown'}). Проверь, что registry-сервер запущен.</div>`;
      return;
    }

    const list = Array.isArray(r.servers) ? r.servers : [];
    if (!list.length) {
      root.innerHTML = '<div class="meta">Активных миров пока нет.</div>';
      return;
    }

    root.innerHTML = list.map((s, i) => {
      const name = String(s.worldName || `Server #${i + 1}`);
      const host = String(s.hostName || 'unknown');
      const ip = String(s.connect?.ip || '');
      const port = Number(s.connect?.port || 19132);
      const ver = String(s.gameVersion || 'bedrock');
      const maxPlayers = Number(s.maxPlayers || 10);
      const currentPlayers = Number(s.currentPlayers || 0);
      const disabled = !ip;
      return `<div class="item">
        <div>
          <div class="name">${name}</div>
          <div class="meta">Host: ${host} • ${ip ? `${ip}:${port}` : 'адрес скрыт'} • v${ver} • ${currentPlayers}/${maxPlayers}</div>
        </div>
        <button class="btn ${disabled ? '' : 'acc'}" data-ip="${ip}" data-port="${port}" ${disabled ? 'disabled' : ''}>Присоединиться</button>
      </div>`;
    }).join('');

    root.querySelectorAll('button[data-ip]').forEach((b) => {
      b.addEventListener('click', async () => {
        const ip = b.getAttribute('data-ip') || '';
        const port = Number(b.getAttribute('data-port') || 19132);
        if (!ip) return;
        await window.noc.shellOpenExternal(`minecraft://?addExternalServer=${encodeURIComponent('Noc Global')}|${ip}:${port}`);
      });
    });
  }

  async function checkBedrockStatus() {
    const s = await window.noc.bedrockHostStatus();
    if (!s?.ok) return;

    hostWanted = !!s.manualHostWanted;
    paintHostToggle();

    if (!s.registryUrl) {
      setHostStatus('Не найден реестр. Подними локальный/внешний registry и он подцепится автоматически.');
      return;
    }

    if (!s.bedrockRunning) {
      setHostStatus(`Реестр: ${s.registryUrl}. Bedrock не запущен. Нажми «Открыть мир».`);
    } else if (!s.worldOpen && !hostWanted) {
      setHostStatus(`Реестр: ${s.registryUrl}. Мягкий режим: включи Хост ON или открой мир для сети.`);
    } else if (s.autoHosting) {
      setHostStatus(`Мир «${s.worldName || 'Bedrock'}» опубликован ✅ Игроки: ${s.currentPlayers || 0}/${s.maxPlayers || 10}`);
    } else {
      setHostStatus(`Публикую мир в реестре...`);
    }
  }

  async function init() {
    $('#btnRefresh')?.addEventListener('click', refresh);
    $('#btnOpenWorld')?.addEventListener('click', async () => {
      await window.noc.bedrockLaunch();
      setTimeout(checkBedrockStatus, 1200);
    });
    $('#btnHostToggle')?.addEventListener('click', async () => {
      hostWanted = !hostWanted;
      await window.noc.localServersHostSetWanted(hostWanted);
      paintHostToggle();
      await checkBedrockStatus();
    });
    $('#btnShareInvite')?.addEventListener('click', async () => {
      const r = await window.noc.localServersInviteCreate();
      if (!r?.ok) {
        setInviteStatus(`Не удалось создать инвайт: ${r?.error || 'unknown'}`);
        return;
      }
      const code = String(r.code || '');
      const link = `noclauncher://join/${code}`;
      try { await navigator.clipboard.writeText(link); setInviteStatus(`Ссылка скопирована: ${link}`); }
      catch { setInviteStatus(`Код приглашения: ${code}`); }
      const inp = $('#inviteCode');
      if (inp) inp.value = code;
    });
    $('#btnJoinByCode')?.addEventListener('click', async () => {
      const code = String($('#inviteCode')?.value || '').trim().toUpperCase();
      if (!code) { setInviteStatus('Введи код приглашения.'); return; }
      const r = await window.noc.localServersInviteResolve(code);
      if (!r?.ok || !r.room) { setInviteStatus(`Код не найден: ${r?.error || 'unknown'}`); return; }
      const ip = String(r.room?.connect?.ip || '');
      const port = Number(r.room?.connect?.port || 19132);
      if (!ip) { setInviteStatus('У хоста нет публичного адреса.'); return; }
      await window.noc.shellOpenExternal(`minecraft://?addExternalServer=${encodeURIComponent(r.room.worldName || 'Noc World')}|${ip}:${port}`);
      setInviteStatus(`Подключение открыто: ${ip}:${port}`);
    });
    $('#btnCloseWin')?.addEventListener('click', () => window.close());

    setInterval(async () => {
      await checkBedrockStatus();
      await refresh();
    }, 4000);

    await checkBedrockStatus();
    await refresh();
  }

  init();
})();
