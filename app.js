
fetch('./dataset.json')
.then(response => response.json())
.then(data => {
    const temp = data.Temperature;
    //console.log(temp)
    const temp_display=document.querySelector('#temp-val');
    temp_display.innerHTML=temp;

    const volt=data.Voltage;
    //console.log(volt)
    const volt_display=document.querySelector('#volt-val');
    volt_display.innerHTML=volt;

    const res=data.Resistance;
    //console.log(res)
    const res_display=document.querySelector('#res-val');
    res_display.innerHTML=res;
})
.catch(error => console.error('Error:', error));
