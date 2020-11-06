function loadpage(){
  document.getElementsByClassName('my_product')[0].style.display = 'none';
  document.getElementsByClassName('my_order')[0].style.display = 'none';
  document.getElementsByClassName('add_raw_mat')[0].style.display = 'none';
}

function showform(a,b,c){
  document.getElementsByClassName(a)[0].style.display = 'inline';
  document.getElementsByClassName(b)[0].style.display = 'none';
  document.getElementsByClassName(c)[0].style.display = 'none';

}
