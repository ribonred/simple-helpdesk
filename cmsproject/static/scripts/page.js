$('a#details').bind('click', function(e){
    var url = $(this).attr('href');
    $('.content').load(url); return false;
    e.preventDefault;

});


$('form').on('change', 'input[type="file"]', function(e) {

    var files = e.target.files,
        f = files[0],
        reader = new FileReader(),
        t = this
    ;

    reader.onload = (function(file) {

        return function(e) {

            $(t).before($('<img>').attr({

                src: e.target.result,
                title: file.name,
                height: "80",
                width: ""
            }));
        };
    })(f);

  reader.readAsDataURL(f);
});


