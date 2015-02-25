
this.ckan.module('timepicker', function ($, _) {
  return {
    options: {
        showMeridian: false,
    },
    
    initialize: function() 
    {
        var module = this
        
        if ($.fn.timepicker) {
            $(this.el).timepicker({
                showMeridian: this.options.showMeridian,
            })
        }
        
        window.console.debug('Initialized module: timepicker')
    },

    teardown: function() 
    { 
        window.console.debug('Tearing down module: timepicker')
    },
  }
});

