$(document).ready(function(){
    $('#btn_translate').click(fetchTranslation);
    $('#language_code').keypress(function(event){
        if(event.which === 13){
            fetchTranslation();
        }
    });

    function fetchTranslation(){
        var languageCode = $('#language_code').val();
        var apiUrl = 'https://fourtonfish.com/hellosalut/?lang=' + languageCode;

        $.get(apiUrl)
            .done(function(data){
                updateHello(data.hello);
            })
            .fail(function(jqxhr, textStatus, error){
                handleError(error);
            });
    }

    function updateHello(message){
        $('#hello').text(message);
    }

    function handleError(error){
        $('#hello').text('Error: ' + error);
    }
});
