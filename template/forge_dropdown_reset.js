'use strict';

(function () {
	function closeAllDropdowns() {
		if (window.jQuery && window.phpbb && typeof window.phpbb.toggleDropdown === 'function') {
			window.jQuery(window.phpbb.dropdownHandles).each(function () {
				window.phpbb.toggleDropdown.call(this);
			});
		}

		var containers = document.querySelectorAll('.dropdown-container, .responsive-menu');
		containers.forEach(function (el) {
			el.classList.remove('visible');
			el.classList.remove('dropdown-visible');
		});

		var dropdowns = document.querySelectorAll('.dropdown');
		dropdowns.forEach(function (el) {
			el.classList.add('hidden');
			el.classList.remove('dropdown-visible');
			el.style.display = 'none';
		});

		var triggers = document.querySelectorAll('.dropdown-trigger, .dropdown-toggle');
		triggers.forEach(function (el) {
			el.setAttribute('aria-expanded', 'false');
		});
	}

	function hardClose() {
		closeAllDropdowns();
		window.setTimeout(closeAllDropdowns, 0);
		window.setTimeout(closeAllDropdowns, 80);
		window.setTimeout(closeAllDropdowns, 180);
	}

	window.forgeCloseAllDropdowns = closeAllDropdowns;

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', hardClose);
	} else {
		hardClose();
	}

	window.addEventListener('pageshow', hardClose);
	window.addEventListener('popstate', hardClose);
	window.addEventListener('pagehide', closeAllDropdowns);
	window.addEventListener('focus', hardClose);

	document.addEventListener('visibilitychange', function () {
		if (document.visibilityState === 'visible') {
			hardClose();
		}
	});

	document.addEventListener('click', function (event) {
		var link = event.target && event.target.closest ? event.target.closest('.dropdown-contents a') : null;
		if (link) {
			closeAllDropdowns();
		}
	}, true);
})();
