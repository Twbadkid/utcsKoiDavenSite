$("#show-nav").click(function() // 觸發展開目錄
{
   if( $(this).hasClass("nav-on-show") ) // 當已經是展開== 縮回去
   {
      $(this).removeClass("nav-on-show");
      $("#mobile-screen").animate( { left: '-=250'} , 250 , function() {} );
   }
   else // 當不是展開時== 展開
   {
      $(this).addClass("nav-on-show");
      $("#mobile-screen").animate( { left: '+=250'} , 250 , function() {} );
   }
});
$("#mobile-screen").height( document.documentElement.clientHeight); // 將畫面高度填滿實際可見高度

window.fbAsyncInit = function() {
    FB.init({
      appId      : '463703423771173',
      xfbml      : true,
      version    : 'v2.1'
    });
  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "//connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));
</script> 
<script type="text/javascript">
function getBrowserHeight()
{
var intH = 0;
var intW = 0;

if(typeof window.innerWidth == 'number' )
{
intH = window.innerHeight;
intW = window.innerWidth;
}
else if(document.documentElement && (document.documentElement.clientWidth || document.documentElement.clientHeight))
{
intH = document.documentElement.clientHeight;
intW = document.documentElement.clientWidth;
}
else if(document.body && (document.body.clientWidth || document.body.clientHeight))
{
intH = document.body.clientHeight;
intW = document.body.clientWidth;
}
return { width: parseInt(intW), height: parseInt(intH) };
}

function setLayerPosition()
{
var shadow = document.getElementById('shadow');
var question = document.getElementById('question');
var bws = getBrowserHeight();

shadow.style.width = bws.width + 'px';
shadow.style.height = bws.height + 'px';

question.style.left = parseInt((bws.width - 350) / 2);
question.style.top = parseInt((bws.height - 200) / 2);

shadow = null;
question = null;
}

function showLayer()
{
setLayerPosition();

var shadow = document.getElementById('shadow');
var question = document.getElementById('question');

shadow.style.display = 'block';
question.style.display = 'block';

shadow = null;
question = null;
}

function hideLayer()
{
var shadow = document.getElementById('shadow');
var question = document.getElementById('question');

shadow.style.display = 'none';
question.style.display = 'none';

shadow = null;
question = null;
}
window.onresize = setLayerPosition;

var main = function() {
  $('.dropdown-toggle').click(function() {
    $('.dropdown-menu').toggle();
  });
}

$(document).ready(main);
