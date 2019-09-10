var userOptions = [];

//unit option
$('.go-btn').click(function() {
    var unit = $('#unit-dropdown option:selected');
    console.log(unit.val())
    userOptions.push(unit.val());
    var bed = $('#bed-dropdown option:selected');
    userOptions.push(bed.val());
    var bth = $('#bath-dropdown option:selected');
    userOptions.push(bth.val());
    var pet = $('#pet-dropdown option:selected');
    userOptions.push(pet.val());
    var fur = $('#fur-dropdown option:selected');
    userOptions.push(fur.val());
    var par = $('#par-dropdown option:selected');
    userOptions.push(par.val());
    var air = $('#air-dropdown option:selected');
    userOptions.push(air.val());
    var smo = $('#smo-dropdown option:selected');
    userOptions.push(smo.val());
    console.log(smo.val())
    var reg = $('#selectRegion option:selected');
    //console.log(reg)
    userOptions.push(reg.val());

    console.log(userOptions);
});


