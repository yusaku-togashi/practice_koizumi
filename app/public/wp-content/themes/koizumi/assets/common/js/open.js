// JavaScript Document
window.onload = function() {
	var node_a = document.getElementsByTagName('a');
	for (var i in node_a) {
		if (node_a[i].className == 'newwin') {
			node_a[i].onclick = function() {
				window.open(this.href, '', '');
				return false;
			};
		}
	}
};
