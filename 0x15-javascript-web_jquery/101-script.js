// Add an element, remove the last one and delete everything
$(document).ready(()=>{
    $('DIV#add_item').click(()=>{
        $('UL.my_list').append('<li>Item</li>');
    });
    $('DIV#remove_item').click(()=>{
        $('UL.my_list li').last().remove();
    });
    $('DIV#clear_list').click(()=>{
        $('UL.my_list').empty();
    });
});
