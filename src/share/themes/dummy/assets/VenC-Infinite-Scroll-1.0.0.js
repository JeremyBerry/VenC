var VENC_INFINITE_SCROLL = {
	queue: 0,
	hideVenCNavigation: true,
	pageOffset : 0,
	xmlhttp : Object,
	timer: Object,
	imageDefaultSetup: function(img) {
		img.style.opacity = "0.0";
	},
	entryDefautSetup: function(entry) {
		entry.style.opacity = "0.0";
	},
	onLoadImage: function(img) {
		img.style.transition = "opacity 0.5s ease";
		img.style.opacity = "1.0";
	},
	onLoadEntry: function(entry){
		entry.style.transition = "opacity 0.5s ease";
		entry.style.opacity = "1.0";
	},
	loading : function() {
		try {
			document.getElementById("__VENC_LOADING__").style.opacity = "1";
		}
		catch (e) {
			console.log("VenC: There is no __VENC_LOADING__ element.");
		}
	},
	idle : function() {
		try {
			document.getElementById("__VENC_LOADING__").style.opacity = "0";
		}
		catch (e) {
			console.log("VenC: There is no __VENC_LOADING__ element.");
		}
	},
	initPageOffset : function() {
		currentFilename = window.location.pathname.split('/')[window.location.pathname.split('/').length-1];
		if (currentFilename == '' | currentFilename == "index.html")
			currentFilename = '0';
		else if (currentFilename.replace( /[.html0123456789]+/g, '') != "index") {
			return;
		}
        	this.pageOffset = parseInt(currentFilename.replace( /^\D+/g, '').replace( /[.html]+/g,''))+1;
	},
	pushColumns : function() {
		if (window.XMLHttpRequest) { // code for IE7+, Firefox, Chrome, Opera, Safari
			this.xmlhttp = new XMLHttpRequest();
		}
		else { // code for IE6, IE5
			this.xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
		}
		this.xmlhttp.onreadystatechange = this.ajax;
		this.xmlhttp.open("GET","index"+this.pageOffset+".html",true);
		this.pageOffset++;
		this.xmlhttp.send();
	},
	ajax : Object
};

function VENC_INFINITE_SCROLL_AJAX() {
	if (VENC_INFINITE_SCROLL.xmlhttp.readyState == 4 && VENC_INFINITE_SCROLL.xmlhttp.status == 200) {
		xmlDoc = document.implementation.createHTMLDocument('');
		xmlDoc.body.innerHTML = VENC_INFINITE_SCROLL.xmlhttp.responseText;
		currentColumns = document.getElementsByClassName("__VENC_COLUMN__");
		newColumns = xmlDoc.getElementsByClassName("__VENC_COLUMN__");
		for (i=0; i < currentColumns.length; i++) {
			newEntries = newColumns[i].getElementsByClassName("entry");
			entriesClones = Array();
			for (j=0; j < newEntries.length; j++) {
				entriesClones.push( newEntries[j].cloneNode(true));
			}
			for(j=0; j < entriesClones.length; j++) {
				images = entriesClones[j].getElementsByTagName("img");
				for (k=0; k < images.length; k++) {
					VENC_INFINITE_SCROLL.queue++;
					VENC_INFINITE_SCROLL.imageDefaultSetup(images[k]);
					images[k].onload = function(e) {
						VENC_INFINITE_SCROLL.queue--;
						VENC_INFINITE_SCROLL.onLoadImage(this);
					}
					d = new Date()
					images[k].src = images[k].src+"?uglyWorkAround="+d.getTime();
				}
				currentColumns[i].appendChild(entriesClones[j]);
			}
		}
	}
};

function VENC_INFINITE_SCROLL_RUN() {
	if (VENC_INFINITE_SCROLL.queue == 0) {
		VENC_INFINITE_SCROLL.idle();
	}
	else {
		VENC_INFINITE_SCROLL.loading();
	}
	currentColumns = document.getElementsByClassName("__VENC_COLUMN__");
	viewPortHeight = Math.max(document.documentElement.clientHeight, window.innerHeight || 0);
	for (i=0; i < currentColumns.length; i++) {
		if (currentColumns[i].clientHeight <= viewPortHeight + window.pageYOffset) {
			if (VENC_INFINITE_SCROLL.queue == 0) {
				VENC_INFINITE_SCROLL.pushColumns();
				return 1;
			}
		}
	}
	return 0;
};

function VENC_INFINITE_SCROLL_ON_LOAD() {
	VENC_INFINITE_SCROLL.initPageOffset()
	if (VENC_INFINITE_SCROLL.hideVenCNavigation) {
       		try {
	 	 	document.getElementById("__VENC_NAVIGATION__").setAttribute("style","display: none;");
		}
       		catch (e) {
       			console.log("VenC: There is no __VENC_NAVIGATION__ element.");
       		}
	}
	VENC_INFINITE_SCROLL.ajax = VENC_INFINITE_SCROLL_AJAX;
	VENC_INFINITE_SCROLL.timer = setInterval(VENC_INFINITE_SCROLL_RUN, 250);
};
