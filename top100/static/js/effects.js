$(document).ready(function() {

  $("div.songs > h1.content-subhead").click(function () {
    $("div.song-description").slideUp();
  });

  $("div.songs > h1.content-subhead").dblclick(function () {
    $("div.song-description").slideDown();
  });
  
 });