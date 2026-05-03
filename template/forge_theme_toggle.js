/*!
 * ForgeBoard theme toggle — light / dark / auto.
 * Persists choice in localStorage AND a cookie (server-readable, 1 year).
 * Sets data-theme on <html> so CSS can react via [data-theme="dark"].
 *
 * Markup expected:
 *   <button class="forge-theme-toggle" data-theme-toggle aria-label="...">
 *
 * GPL-2.0 (c) 2026 FanFanLaTuFlippe
 */
(function () {
	'use strict';

	var STORAGE_KEY = 'forgeboard_theme';
	var COOKIE_NAME = 'forgeboard_theme';

	function readCookie(name) {
		var match = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
		return match ? decodeURIComponent(match[1]) : null;
	}

	function writeCookie(name, value) {
		var oneYear = 60 * 60 * 24 * 365;
		document.cookie = name + '=' + encodeURIComponent(value) +
			'; max-age=' + oneYear +
			'; path=/; SameSite=Lax';
	}

	function getStored() {
		try {
			return localStorage.getItem(STORAGE_KEY) || readCookie(COOKIE_NAME);
		} catch (e) {
			return readCookie(COOKIE_NAME);
		}
	}

	function setStored(value) {
		try {
			if (value === 'auto') {
				localStorage.removeItem(STORAGE_KEY);
			} else {
				localStorage.setItem(STORAGE_KEY, value);
			}
		} catch (e) { /* localStorage blocked */ }
		writeCookie(COOKIE_NAME, value);
	}

	function resolveTheme(stored) {
		if (stored === 'dark' || stored === 'light') return stored;
		// auto / null -> follow system
		var prefersDark = window.matchMedia &&
			window.matchMedia('(prefers-color-scheme: dark)').matches;
		return prefersDark ? 'dark' : 'light';
	}

	function applyTheme(stored) {
		var resolved = resolveTheme(stored);
		var root = document.documentElement;
		root.setAttribute('data-theme', resolved);
		root.setAttribute('data-theme-pref', stored || 'auto');
	}

	// 1. Apply on load (before any user interaction)
	var current = getStored() || 'auto';
	applyTheme(current);

	// 2. Listen to system theme change when in auto mode
	if (window.matchMedia) {
		var mq = window.matchMedia('(prefers-color-scheme: dark)');
		var sysListener = function () {
			if ((getStored() || 'auto') === 'auto') {
				applyTheme('auto');
			}
		};
		if (mq.addEventListener) mq.addEventListener('change', sysListener);
		else if (mq.addListener) mq.addListener(sysListener);
	}

	// 3. Wire up toggle buttons (cycle: auto -> light -> dark -> auto)
	function cycle(value) {
		if (value === 'auto') return 'light';
		if (value === 'light') return 'dark';
		return 'auto';
	}

	function init() {
		var triggers = document.querySelectorAll('[data-theme-toggle]');
		Array.prototype.forEach.call(triggers, function (btn) {
			btn.addEventListener('click', function (e) {
				e.preventDefault();
				var stored = getStored() || 'auto';
				var next = cycle(stored);
				setStored(next);
				applyTheme(next);
			});
		});
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', init);
	} else {
		init();
	}

	// Public API for other scripts
	window.ForgeTheme = {
		set: function (value) { setStored(value); applyTheme(value); },
		get: function () { return getStored() || 'auto'; },
		resolved: function () { return resolveTheme(getStored() || 'auto'); }
	};
})();
