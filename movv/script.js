/* begin Page */
/* Created by Artisteer v3.1.0.42580 */

// css hacks
(function($) {
    // fix ie blinking
    var m = document.uniqueID && document.compatMode && !window.XMLHttpRequest && document.execCommand;
    try { if (!!m) { m('BackgroundImageCache', false, true); } }
    catch (oh) { };
    // css helper
    var data = [
        {str:navigator.userAgent,sub:'Chrome',ver:'Chrome',name:'chrome'},
        {str:navigator.vendor,sub:'Apple',ver:'Version',name:'safari'},
        {prop:window.opera,ver:'Opera',name:'opera'},
        {str:navigator.userAgent,sub:'Firefox',ver:'Firefox',name:'firefox'},
        {str:navigator.userAgent,sub:'MSIE',ver:'MSIE',name:'ie'}];
    for (var n=0;n<data.length;n++)	{
        if ((data[n].str && (data[n].str.indexOf(data[n].sub) != -1)) || data[n].prop) {
            var v = function(s){var i=s.indexOf(data[n].ver);return (i!=-1)?parseInt(s.substring(i+data[n].ver.length+1)):'';};
            $('html').addClass(data[n].name+' '+data[n].name+v(navigator.userAgent) || v(navigator.appVersion)); break;			
        }
    }
})(jQuery);

var _artStyleUrlCached = null;
function artGetStyleUrl() {
    if (null == _artStyleUrlCached) {
        var ns;
        _artStyleUrlCached = '';
        ns = jQuery('link');
        for (var i = 0; i < ns.length; i++) {
            var l = ns[i].href;
            if (l && /style\.ie6\.css(\?.*)?$/.test(l))
                return _artStyleUrlCached = l.replace(/style\.ie6\.css(\?.*)?$/, '');
        }
        ns = jQuery('style');
        for (var i = 0; i < ns.length; i++) {
            var matches = new RegExp('import\\s+"([^"]+\\/)style\\.ie6\\.css"').exec(ns[i].html());
            if (null != matches && matches.length > 0)
                return _artStyleUrlCached = matches[1];
        }
    }
    return _artStyleUrlCached;
}

function artFixPNG(element) {
    if (jQuery.browser.msie && parseInt(jQuery.browser.version) < 7) {
		var src;
		if (element.tagName == 'IMG') {
			if (/\.png$/.test(element.src)) {
				src = element.src;
				element.src = artGetStyleUrl() + 'images/spacer.gif';
			}
		}
		else {
			src = element.currentStyle.backgroundImage.match(/url\("(.+\.png)"\)/i);
			if (src) {
				src = src[1];
				element.runtimeStyle.backgroundImage = 'none';
			}
		}
		if (src) element.runtimeStyle.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(src='" + src + "')";
	}
}

jQuery(function() {
	if (!jQuery('html').hasClass('ie7')) return; //ie7 only
    jQuery('div.box').each(function(){
    	var b = jQuery(this);
    	jQuery.each('br|bl|cr|cl|tr|tl'.split('|'), function(){b.prepend('<div class="box-'+this+'"> </div>');});	
    });
    jQuery('div.bar').each(function(){
    	var b = jQuery(this);
    	jQuery.each('r|l'.split('|'), function(){b.prepend('<div class="bar-'+this+'"> </div>');});	
    });
    jQuery('div.footer').each(function(){
    	var b = jQuery(this);
    	jQuery.each('r|l|t'.split('|'), function(){b.prepend('<div class="footer-'+this+'"> </div>');});	
    });
    jQuery('ul.hmenu>li>a').each(function(){
    	var b = jQuery(this);
    	jQuery.each('r|l'.split('|'), function(){b.prepend('<span class="hmenu-'+this+'"> </span>');});	
    });
    jQuery('div.layout-wrapper>div.content-layout>div.content-layout-row>div.layout-cell:not(.content)').each(function(){
    	jQuery(this).append('<div class="sidebar-bg" ><div class="sidebar-bg-inner" > </div></div>')
    });
    jQuery('ul.vmenu>li>a').each(function(){
    	var b = jQuery(this);
    	jQuery.each('r|l'.split('|'), function(){b.prepend('<span class="vmenu-'+this+'"> </span>');});	
    });
    jQuery('ul.vmenu ul a').each(function(){
    	jQuery(this).prepend('<span class="vmenu-icon"> </span>');	
    });
});
/* end Page */

/* begin Menu */
jQuery(function () {
    if (!jQuery.browser.msie || parseInt(jQuery.browser.version) > 7) return;
    jQuery('ul.hmenu>li:not(:first-child)').each(function () { jQuery(this).prepend('<span class="hmenu-separator"> </span>'); });
    if (!jQuery.browser.msie || parseInt(jQuery.browser.version) > 6) return;
    jQuery('ul.hmenu li').each(function () {
        this.j = jQuery(this);
        this.UL = this.j.children('ul:first');
        if (this.UL.length == 0) return;
        this.A = this.j.children('a:first');
        this.onmouseenter = function () {
            this.j.addClass('hmenuhover');
            this.UL.addClass('hmenuhoverUL');
            this.A.addClass('hmenuhoverA');
        };
        this.onmouseleave = function() {
            this.j.removeClass('hmenuhover');
            this.UL.removeClass('hmenuhoverUL');
            this.A.removeClass('hmenuhoverA');
        };
    });
});

jQuery(function() { setHMenuOpenDirection({container: "div.sheet-body", defaultContainer: "#main", menuClass: "hmenu", leftToRightClass: "hmenu-left-to-right", rightToLeftClass: "hmenu-right-to-left"}); });

function setHMenuOpenDirection(menuInfo) {
    var defaultContainer = jQuery(menuInfo.defaultContainer);
    defaultContainer = defaultContainer.length > 0 ? defaultContainer = jQuery(defaultContainer[0]) : null;

    jQuery("ul." + menuInfo.menuClass + ">li>ul").each(function () {
        var submenu = jQuery(this);
        var submenuWidth = submenu.outerWidth();
        var submenuLeft = submenu.offset().left;

        var mainContainer = submenu.parents(menuInfo.container);
        mainContainer = mainContainer.length > 0 ? mainContainer = jQuery(mainContainer[0]) : null;

        var container = mainContainer || defaultContainer;
        if (container != null) {
            var containerLeft = container.offset().left;
            var containerWidth = container.outerWidth();

            if (submenuLeft + submenuWidth >=
                    containerLeft + containerWidth) 
                /* right to left */
                submenu.addClass(menuInfo.rightToLeftClass).find("ul").addClass(menuInfo.rightToLeftClass);
            if (submenuLeft <= containerLeft)
                /* left to right */
                submenu.addClass(menuInfo.leftToRightClass).find("ul").addClass(menuInfo.leftToRightClass);
        }
    });
}
/* end Menu */

/* begin MenuSubItem */
jQuery(function () {
    if (!jQuery.browser.msie) return;
    var ieVersion = parseInt(jQuery.browser.version);
    if (ieVersion > 7) return;

    /* Fix width of submenu items.
    * The width of submenu item calculated incorrectly in IE6-7. IE6 has wider items, IE7 display items like stairs.
    */
    jQuery.each(jQuery("ul.hmenu ul"), function () {
        var maxSubitemWidth = 0;
        var submenu = jQuery(this);
        var subitem = null;
        jQuery.each(submenu.children("li").children("a"), function () {
            subitem = jQuery(this);
            var subitemWidth = subitem.outerWidth();
            if (maxSubitemWidth < subitemWidth)
                maxSubitemWidth = subitemWidth;
        });
        if (subitem != null) {
            if (ieVersion < 7)
                maxSubitemWidth += 12; // default text indent
            else {
                var subitemBorderLeft = parseInt(subitem.css("border-left-width"), 10) || 0;
                var subitemBorderRight = parseInt(subitem.css("border-right-width"), 10) || 0;
                var subitemPaddingLeft = parseInt(subitem.css("padding-left"), 10) || 0;
                var subitemPaddingRight = parseInt(subitem.css("padding-right"), 10) || 0;
                maxSubitemWidth -= subitemBorderLeft + subitemBorderRight + subitemPaddingLeft + subitemPaddingRight;
            }

            submenu.children("li").children("a").css("width", maxSubitemWidth + "px");
        }
    });

    if (ieVersion > 6) return;
    jQuery("ul.hmenu ul>li:first-child>a").css("border-top-width", "1px");
});
/* end MenuSubItem */

/* begin Box, Sheet */

function artFluidSheetComputedWidth(percent, minval, maxval) {
    percent = parseInt(percent);
    var val = document.body.clientWidth / 100 * percent;
    return val < minval ? minval + 'px' : val > maxval ? maxval + 'px' : percent + '%';
}/* end Box, Sheet */

/* begin Layout */
jQuery(function () {
     var c = jQuery('div.content');
    if (c.length !== 1) return;
    var s = c.parent().children('.layout-cell:not(.content)');
    jQuery(window).bind('resize', function () {
        c.css('height', 'auto');
        var r = jQuery(window).height() - jQuery('#main').height();
        if (r > 0) c.css('height', r + c.height() + 'px');
    });

    if (jQuery.browser.msie && parseInt(jQuery.browser.version) < 8) {

        jQuery(window).bind('resize', function () {
            var w = 0;
            c.hide();
            s.each(function () { w += this.clientWidth; });
            c.w = c.parent().width(); c.css('width', c.w - w + 'px');
            c.show();
        })

        var r = jQuery('div.content-layout-row').each(function () {
            this.c = jQuery(this).children('.layout-cell:not(.content)');
        });

        jQuery(window).bind('resize', function () {
            r.each(function () {
                if (this.h == this.clientHeight) return;
                this.c.css('height', 'auto');
                var r = jQuery(window).height() - jQuery('#main').height();
                this.h = this.clientHeight;
                if (r > 0) this.h += r;
                this.c.css('height', this.h + 'px');
            });
        });
    }

    var g = jQuery('.layout-glare-image');
    jQuery(window).bind('resize', function () {
        g.each(function () {
            var i = jQuery(this);
            i.css('height', i.parents('.layout-cell').height() + 'px');
        });
    });

    jQuery(window).trigger('resize');
});/* end Layout */

/* begin Button */
function artButtonSetup(className) {
    jQuery.each(jQuery("a." + className + ", button." + className + ", input." + className), function (i, val) {
        var b = jQuery(val);
        if (!b.parent().hasClass('button-wrapper')) {
            if (b.is('input')) b.val(b.val().replace(/^\s*/, '')).css('zoom', '1');
            if (!b.hasClass('button')) b.addClass('button');
            jQuery("<span class='button-wrapper'><span class='button-l'> </span><span class='button-r'> </span></span>").insertBefore(b).append(b);
            if (b.hasClass('active')) b.parent().addClass('active');
        }
        b.mouseover(function () { jQuery(this).parent().addClass("hover"); });
        b.mouseout(function () { var b = jQuery(this); b.parent().removeClass("hover"); if (!b.hasClass('active')) b.parent().removeClass('active'); });
        b.mousedown(function () { var b = jQuery(this); b.parent().removeClass("hover"); if (!b.hasClass('active')) b.parent().addClass('active'); });
        b.mouseup(function () { var b = jQuery(this); if (!b.hasClass('active')) b.parent().removeClass('active'); });
    });
}
jQuery(function() { artButtonSetup("button"); });

/* end Button */



