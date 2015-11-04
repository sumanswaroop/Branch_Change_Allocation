$(document).ready(function(){
	var previous = new Array(16);
	var first = true;
    var not1 = $("#id_Present_Branch").val();
    prev = not1;
    if($("#id_Present_Branch").val()!='')
    {
        $('#id_Present_Branch option:not(:selected)').attr('disabled', true);
        $('#id_Category option:not(:selected)').attr('disabled', true);
        $('#id_name').attr('readonly', true);
        $('#id_cpi').attr('readonly', true);

    }
    for(var e = 1 ; e<=16;e++)
    {           
                var d = e.toString();
                if ($("#id_Preference_" + d).val()==''){
                	if(first == true){first = false;}
               else{
                $("#Preference"+d).css("display", "none");
            }
				}
				if(not1 != ''){
                $("#id_Preference_"+d+ " option[value="+"'"+ not1 + "'" + "]").remove();
            }

                previous[e-1] = $("#id_Preference_" + d).val();
                
    }
    
    $(document).on('change',"#id_Present_Branch",function(){
        
        not1 = $("#id_Present_Branch").val();
         for(var e = 1 ; e<=16;e++)
    {           
                var d = e.toString();
                $("#id_Preference_"+d+ " option[value="+"'"+ not1 + "'" + "]").remove();
                $("#id_Preference_"+d+ " option[value="+"'"+ prev + "'" + "]").add();
                
    }
    prev = not1;
    alert("Please be Careful.Once Submitted,You Wont be Allowed to Change Name,CPI , Present Branch, and Category Field.");
        
    });
    $(document).on('click',"#id_refresh",function(){
        
 
         for(var e = 1 ; e<=16;e++)
    {           
                var d = e.toString();
                 $("#id_Preference_" + d).val('');
                 $("#Preference"+d).css("display", "none");
                
    }
        $("#Preference1").css("display", "block");
    });

    $(document).on('change',"#id_Preference_1",function(){
    	if($.trim($("#id_Preference_1").val()) == '')
    	{
            for(var i =2 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }

        
    }
    else 
    {   
       var ne = $("#id_Preference_1").val();
       $("#Preference2").css("display", "block");
       for(var i =1 ; i<=16;i++)
            {   
                if(i==1)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {
                    if(previous[0]!='')
                  {      
                    $("#id_Preference_"+t).val(previous[0]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[0] = ne;
                    previous[i-1] = exist;
                    break;

                }
                else {
                    $("#id_Preference_1").val('');
                    alert("You have already chosen that option");
                    $("#Preference2").css("display", "none");

                }

                }
                
            }

    }
    });

    $(document).on('change',"#id_Preference_2",function(){
        if($.trim($("#id_Preference_2").val()) == '')
        {
            for(var i =3 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference3").css("display", "block");
       var ne = $("#id_Preference_2").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==2)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {
                    if(previous[1]!='')
                    {
                    $("#id_Preference_"+t).val(previous[1]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[1] = ne;
                    previous[i-1] = exist;
                    break;
                }

                     else {
                    $("#id_Preference_2").val('');
                    alert("You have already chosen that option");
                    $("#Preference3").css("display", "none");
                    
                }

                }
                
            }
    }
    });


    $(document).on('change',"#id_Preference_3",function(){
        if($.trim($("#id_Preference_3").val()) == '')
        {
            for(var i =4 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference4").css("display", "block"); 
       var ne = $("#id_Preference_3").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==3)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {   
                    if(previous[2]!='')
                    {
                    $("#id_Preference_"+t).val(previous[2]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[2] = ne;
                    previous[i-1] = exist;
                    break;
                }
                 else {
                    $("#id_Preference_3").val('');
                    alert("You have already chosen that option");
                    $("#Preference4").css("display", "none");
                }

                }
                
            }
    }
    });


    $(document).on('change',"#id_Preference_4",function(){
        if($.trim($("#id_Preference_4").val()) == '')
        {
            for(var i =5 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference5").css("display", "block");
       var ne = $("#id_Preference_4").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==4)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {   
                    if(previous[3]!='')
                    {
                    $("#id_Preference_"+t).val(previous[3]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[3] = ne;
                    previous[i-1] = exist;
                    break;
                }
                 else {
                    $("#id_Preference_4").val('');
                    alert("You have already chosen that option");
                    $("#Preference5").css("display", "none");
                }

                }
                
            }
    }
    });


    $(document).on('change',"#id_Preference_5",function(){
        if($.trim($("#id_Preference_5").val()) == '')
        {
            for(var i =6 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference6").css("display", "block");
       var ne = $("#id_Preference_5").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==5)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {
                    if(previous[4]!=''){
                    $("#id_Preference_"+t).val(previous[4]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[4] = ne;
                    previous[i-1] = exist;
                    break;}
                     else {
                    $("#id_Preference_5").val('');
                    alert("You have already chosen that option");
                    $("#Preference6").css("display", "none");
                }

                }
                
            }
    }
    });


    $(document).on('change',"#id_Preference_7",function(){
        if($.trim($("#id_Preference_7").val()) == '')
        {
            for(var i =8 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference8").css("display", "block");
       var ne = $("#id_Preference_7").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==7)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {   if(previous[6]!='')
            {
                    $("#id_Preference_"+t).val(previous[6]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[6] = ne;
                    previous[i-1] = exist;
                    break;
                }
                 else {
                    $("#id_Preference_7").val('');
                    alert("You have already chosen that option");
                    $("#Preference8").css("display", "none");
                }

                }
                
            }
    }
    });


    $(document).on('change',"#id_Preference_6",function(){
        if($.trim($("#id_Preference_6").val()) == '')
        {
            for(var i =7 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference7").css("display", "block"); 
       var ne = $("#id_Preference_6").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==6)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {

                    if(previous[5]!=''){
                    $("#id_Preference_"+t).val(previous[5]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[5] = ne;
                    previous[i-1] = exist;
                    break;
                }
                 else {
                    $("#id_Preference_6").val('');
                    alert("You have already chosen that option");
                    $("#Preference7").css("display", "none");
                }

                }
                
            }
    }
    });


    $(document).on('change',"#id_Preference_8",function(){
        if($.trim($("#id_Preference_8").val()) == '')
        {
            for(var i =9 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference9").css("display", "block");
       var ne = $("#id_Preference_8").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==8)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {   
                    if(previous[7]!=''){
                    $("#id_Preference_"+t).val(previous[7]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[7] = ne;
                    previous[i-1] = exist;
                    break;
}
                     else {
                    $("#id_Preference_8").val('');
                    alert("You have already chosen that option");
                    $("#Preference9").css("display", "none");
                }

                }
                
            }
    }
    });

    $(document).on('change',"#id_Preference_9",function(){
        if($.trim($("#id_Preference_9").val()) == '')
        {
            for(var i =10 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference10").css("display", "block"); 
       var ne = $("#id_Preference_9").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==9)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {
                    if(previous[8]!=''){
                    $("#id_Preference_"+t).val(previous[8]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[8] = ne;
                    previous[i-1] = exist;
                    break;
                }
                     else {
                    $("#id_Preference_9").val('');
                    alert("You have already chosen that option");
                    $("#Preference10").css("display", "none");
                }
                }
                
            }
    }
    });

    $(document).on('change',"#id_Preference_11",function(){
        if($.trim($("#id_Preference_11").val()) == '')
        {
            for(var i =12 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference12").css("display", "block");
       var ne = $("#id_Preference_11").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==11)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {   
                    if(previous[10]!=''){
                    $("#id_Preference_"+t).val(previous[10]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[10] = ne;
                    previous[i-1] = exist;
                    break;
                        }
                     else {
                    $("#id_Preference_11").val('');
                    alert("You have already chosen that option");
                    $("#Preference12").css("display", "none");
                }

                }
                
            }
    }
    });

    $(document).on('change',"#id_Preference_10",function(){
        if($.trim($("#id_Preference_10").val()) == '')
        {
            for(var i =11 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference11").css("display", "block");
       var ne = $("#id_Preference_10").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==10)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {
                    if(previous[9]!=''){
                    $("#id_Preference_"+t).val(previous[9]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[9] = ne;
                    previous[i-1] = exist;
                    break;}

                     else {
                    $("#id_Preference_10").val('');
                    alert("You have already chosen that option");
                    $("#Preference11").css("display", "none");
                }

                }
                
            } 
    }
    });


    $(document).on('change',"#id_Preference_12",function(){
        if($.trim($("#id_Preference_12").val()) == '')
        {
            for(var i =13 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference13").css("display", "block");
       var ne = $("#id_Preference_12").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==12)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {
                    if(previous[11]!=''){
                    $("#id_Preference_"+t).val(previous[11]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[11] = ne;
                    previous[i-1] = exist;
                    break;
                }
                 else {
                    $("#id_Preference_12").val('');
                    alert("You have already chosen that option");
                    $("#Preference13").css("display", "none");
                }
                }
                
            } 
    }
    });

    $(document).on('change',"#id_Preference_13",function(){
        if($.trim($("#id_Preference_13").val()) == '')
        {
            for(var i =13 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference14").css("display", "block");
       var ne = $("#id_Preference_13").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==13)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {   
                    if(previous[12]!=''){
                    $("#id_Preference_"+t).val(previous[12]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[12] = ne;
                    previous[i-1] = exist;
                    break;
                }
                 else {
                    $("#id_Preference_13").val('');
                    alert("You have already chosen that option");
                    $("#Preference14").css("display", "none");
                }

                }
                
            } 
    }
    });


    $(document).on('change',"#id_Preference_14",function(){
        if($.trim($("#id_Preference_14").val()) == '')
        {
            for(var i =15 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference15").css("display", "block");
       var ne = $("#id_Preference_2").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==2)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {   
                    if(previous[13]!=''){
                    $("#id_Preference_"+t).val(previous[13]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[13] = ne;
                    previous[i-1] = exist;
                    break;
                }
                 else {
                    $("#id_Preference_14").val('');
                    alert("You have already chosen that option");
                    $("#Preference15").css("display", "none");
                }

                }
                
            } 
    }
    });


    $(document).on('change',"#id_Preference_15",function(){
        if($.trim($("#id_Preference_15").val()) == '')
        {
            for(var i =16 ; i<=16;i++)
            {
                var t = i.toString();
                $("#id_Preference_" + t).val('');
                $("#Preference"+t).css("display", "none");
            }
        
    }
    else 
    {
       $("#Preference16").css("display", "block");
       var ne = $("#id_Preference_15").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==15)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {
                    if(previous[14]!=''){
                    $("#id_Preference_"+t).val(previous[14]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[14] = ne;
                    previous[i-1] = exist;
                    break;
                }
                     else {
                    $("#id_Preference_15").val('');
                    alert("You have already chosen that option");
                    $("#Preference16").css("display", "none");
                }

                }
                
            } 
    }
     });

    $(document).on('change',"#id_Preference_16",function(){
     
     var ne = $("#id_Preference_16").val();
       for(var i =1 ; i<=16;i++)
            {   
                if(i==16)continue;
                var t = i.toString();
                var exist = $("#id_Preference_" + t).val();
                if(exist == ne)
                {   
                    if(previous[15]!=''){
                    $("#id_Preference_"+t).val(previous[15]);
                    alert("Two Fields have same Value. Correcting.");
                    previous[15] = ne;
                    previous[i-1] = exist;
                    break;
                }
                 else {
                    $("#id_Preference_16").val('');
                    alert("You have already chosen that option");
                    
                }

                }
                
            }   
    });
    
});