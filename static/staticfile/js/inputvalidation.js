$(document).ready(function() {
    $('#bchangeform').bootstrapValidator({
        
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields:{
             name:{
                validators:{
                    notEmpty:{
                        message: 'Name can not be empty'
                    }
                }
            },
            rollno:{
                validators:{
                    notEmpty:{
                        message: 'Roll No field is empty'
                    },
                    stringLength:{
                        min:9,
                        max:9,
                        message: 'Roll Number must be of 9 Digits'
                    },
                    regexp:{
                        regexp: /^[1]{1,1}[5]{1,1}[D0-9]{1,1}[0-9]{6,6}/,
                        message: 'Roll Number must be of the form 15XXXXXXX only'

                    }
             }
            },
            cpi:{
                validators:{
                    notEmpty:{
                        message: 'CPI can\'t be empty'
                    },
                    between:{
                        min: 0,
                        max: 10,
                        message: 'CPI must be in [0,10]'
                    },
                    regexp:
                    {
                        regexp:/^\d+(\.\d{1,2})?$/ ,
                        message: "CPI Must be of the form XX.XX"
                    }
                }
            },
            username:{
                validators:{
                    notEmpty:{
                        message: 'Username Can\'t be Empty'
                    },
                    stringLength:{
                        min: 6,
                        max: 30,
                        message: 'Length must be between [6-30]'
                    },
                    regexp:
                    {
                        regexp:/^\S*$/ ,
                        message: "Spaces are not allowed."
                    }
                }
            },
            Preference_1:{
                validators:{
                    notEmpty:{
                        message:'Prefernce can not be empty'
                    }

                }
            },
            pbranch:{
                validators:{
                    notEmpty:{
                        message:'Present Branch can not be empty'
                    }

                }

            }

        }


    });
     

});