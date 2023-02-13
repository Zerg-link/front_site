var app = new Vue({
    el: '#floorss',
    data: {
        floorList: [
            {id: 0, name: 'Подвал', fcount: 0},
            {id: 1, name: '1 Этаж', fcount: 0},
        ],
        NextFloor: 2
    },
    methods: {
        addFloor: function()
        {
            this.floorList.push({id: this.NextFloor, name: this.NextFloor + ' Этаж', fcount: 0});
            this.NextFloor++;
        },
        chFloor: function(id)
        {
            this.floorList[id].fcount = count;
            reset();
        }
    }
})