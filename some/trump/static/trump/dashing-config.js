var dashboard = new Dashboard();

dashboard.addWidget('clock_widget', 'Clock');


dashboard.addWidget('buzzwords_widget', 'List', {
    row: 1,
    getData: function() {
        $.extend(this.scope, {
            title: 'Trump says the darndest things',
            moreInfo: '# of times said around the white house',
            data: [{label: 'Fake News', value: 42},
                   {label: 'The Wall', value: 500},
                   {label: 'Dreamers', value: 55},
                ]
        });
    }
});
