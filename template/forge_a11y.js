/*!
 * ForgeBoard a11y helpers
 *  - Sync aria-expanded on .dropdown-trigger when phpBB toggles
 *    .dropdown-visible on the parent .dropdown-container
 *  - Announce theme toggle state changes via aria-label updates
 *  - Trap focus inside phpbb_alert / phpbb_confirm modals when shown
 *
 * GPL-2.0 (c) 2026 FanFanLaTuFlippe
 */
(function () {
	'use strict';

	/* ----- 1. Dropdown aria-expanded sync ------------------------------ */
	function syncDropdownState(container) {
		var visible = container.classList.contains('dropdown-visible') ||
			container.classList.contains('visible');
		var trigger = container.querySelector('.dropdown-trigger');
		if (trigger) {
			trigger.setAttribute('aria-expanded', visible ? 'true' : 'false');
		}
	}

	function initDropdownAria() {
		var containers = document.querySelectorAll('.dropdown-container');
		Array.prototype.forEach.call(containers, function (c) {
			// Initial state
			syncDropdownState(c);
			// Observe class changes
			if (window.MutationObserver) {
				var mo = new MutationObserver(function (muts) {
					muts.forEach(function (m) {
						if (m.attributeName === 'class') syncDropdownState(c);
					});
				});
				mo.observe(c, { attributes: true });
			}
		});
	}

	/* ----- 2. Theme toggle aria-label dynamic ------------------------- */
	function syncThemeLabel() {
		var btn = document.querySelector('[data-theme-toggle]');
		if (!btn) return;
		var pref = document.documentElement.getAttribute('data-theme-pref') || 'auto';
		var labels = (typeof styleLang === 'object' && styleLang) ? {
			auto: styleLang.auto,
			light: styleLang.light,
			dark: styleLang.dark
		} : {
			auto: 'Theme: auto (follow system) — click to switch to light',
			light: 'Theme: light — click to switch to dark',
			dark: 'Theme: dark — click to switch to auto'
		};
		btn.setAttribute('aria-label', labels[pref] || labels.auto);
	}

	function initThemeAria() {
		syncThemeLabel();
		// Observe data-theme-pref changes on <html>
		if (window.MutationObserver) {
			var mo = new MutationObserver(syncThemeLabel);
			mo.observe(document.documentElement, {
				attributes: true,
				attributeFilter: ['data-theme-pref']
			});
		}
	}

	/* ----- 3. Modal focus trap (phpbb_alert / phpbb_confirm) ----------- */
	var FOCUSABLE = 'a[href], button:not([disabled]), input:not([disabled]):not([type="hidden"]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])';
	var lastFocus = null;

	function trapFocus(modal) {
		var nodes = modal.querySelectorAll(FOCUSABLE);
		if (!nodes.length) return;
		var first = nodes[0];
		var last = nodes[nodes.length - 1];
		modal.addEventListener('keydown', function (e) {
			if (e.key !== 'Tab') return;
			if (e.shiftKey && document.activeElement === first) {
				e.preventDefault();
				last.focus();
			} else if (!e.shiftKey && document.activeElement === last) {
				e.preventDefault();
				first.focus();
			}
		});
	}

	function initModalA11y() {
		var modals = document.querySelectorAll('#phpbb_alert, #phpbb_confirm');
		Array.prototype.forEach.call(modals, function (modal) {
			if (window.MutationObserver) {
				var mo = new MutationObserver(function () {
					var visible = modal.style.display !== 'none' && modal.offsetParent !== null;
					if (visible) {
						lastFocus = document.activeElement;
						var first = modal.querySelector(FOCUSABLE);
						if (first) first.focus();
						trapFocus(modal);
						// Allow Escape to close
						modal.addEventListener('keydown', function escClose(e) {
							if (e.key === 'Escape') {
								var close = modal.querySelector('.alert_close');
								if (close) close.click();
								modal.removeEventListener('keydown', escClose);
							}
						});
					} else if (lastFocus) {
						try { lastFocus.focus(); } catch (e) {}
						lastFocus = null;
					}
				});
				mo.observe(modal, { attributes: true, attributeFilter: ['style', 'class'] });
			}
		});
	}

	/* ----- Boot --------------------------------------------------------- */
	function init() {
		initDropdownAria();
		initThemeAria();
		initModalA11y();
	}

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', init);
	} else {
		init();
	}
})();
