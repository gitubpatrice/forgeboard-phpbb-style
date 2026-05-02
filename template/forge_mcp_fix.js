(function () {
	"use strict";

	if (!document.body || !document.body.classList.contains("section-mcp")) {
		return;
	}

	document.addEventListener(
		"click",
		function (e) {
			var input = e.target.closest('input[type="checkbox"], input[type="radio"]');
			if (input) {
				return;
			}

			var cell = e.target.closest(".forge-mcp-mark-cell, .section-mcp .topiclist dd.mark");
			if (!cell) {
				return;
			}

			if (e.target.closest("a, button, select, option, textarea")) {
				return;
			}

			var target = cell.querySelector('input[type="checkbox"], input[type="radio"]');
			if (!target || target.disabled) {
				return;
			}

			target.checked = !target.checked;
			target.dispatchEvent(new Event("change", { bubbles: true }));
			e.preventDefault();
			e.stopPropagation();
		},
		true
	);
})();
