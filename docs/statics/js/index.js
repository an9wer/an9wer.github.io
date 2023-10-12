switch (window.location.pathname) {
	case "/moments.html":
		document.getElementById("moments").classList.add("active");
		break;
	case "/tools.html":
		document.getElementById("tools").classList.add("active");
		break;
	case "/about.html":
		document.getElementById("about").classList.add("active");
		break;
	default:
		document.getElementById("posts").classList.add("active");
}
