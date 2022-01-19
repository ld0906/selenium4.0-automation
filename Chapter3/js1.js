var domlist = document.getElementsByTagName("input");
    var checkboxlist = [];
    var len = domlist.length;

    for (var i = 0; i < len; i++) {
            if(domlist[i].type == "checkbox"){
                    checkboxlist.push(domlist[i])
            }
    }
