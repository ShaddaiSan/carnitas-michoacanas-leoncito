/* Estado "abierto ahora" + día actual resaltado. Hora de Montréal. Sin dependencias. */
(function () {
  var el = document.getElementById("status");
  if (!el || !window.Intl) return;
  try {
    var parts = new Intl.DateTimeFormat("en-CA", {
      timeZone: "America/Toronto", weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false
    }).formatToParts(new Date());
    var get = function (t) { return parts.filter(function (p) { return p.type === t; })[0].value; };
    var days = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
    var day = days[get("weekday")];
    var mins = (parseInt(get("hour"), 10) % 24) * 60 + parseInt(get("minute"), 10);
    var isOpen = day !== 2 && mins >= 600 && mins < 1260; // 10:00–21:00, cerrado martes
    el.textContent = isOpen ? el.dataset.open : (day === 2 ? el.dataset.tue : (mins < 600 ? el.dataset.opens : el.dataset.closed));
    if (!isOpen) el.classList.add("is-closed");
    var row = document.querySelector('.hours tr[data-day="' + day + '"]');
    if (row) row.classList.add("today");
  } catch (e) { /* sin estado: la página funciona igual */ }
})();
