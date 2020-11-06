
function loadpage(){
  document.getElementsByClassName('add_crop')[0].style.display = 'none';
  document.getElementsByClassName('upd_quant')[0].style.display = 'none';
  document.getElementsByClassName('order')[0].style.display = 'none';
  document.getElementsByClassName('crop_table')[0].style.display = 'none';
  document.getElementsByClassName('buy_raw')[0].style.display = 'none';
}

function showform(a,b,c,d,e){
  document.getElementsByClassName(a)[0].style.display = 'inline';
  document.getElementsByClassName(b)[0].style.display = 'none';
  document.getElementsByClassName(c)[0].style.display = 'none';
  document.getElementsByClassName(d)[0].style.display = 'none';
  document.getElementsByClassName(e)[0].style.display = 'none';
}
