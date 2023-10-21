var modal_loaded = []

$(document).ready(function(){
	$("#search-btn").on('click',function(event){
		$.ajax({
		  type : 'POST',
		  url : "/video",
		  data:{
			query:$("#url-query").val()
		  },
		});
		event.preventDefault();
		$("#loading_wrap").css("display", "block")

	});
});


$(document).ready(function () {
	var socket = io.connect();
	socket.on("updateVideos", function (videos) {
		$("#show-video").empty()
		$("#show-video").append(videos.videos)
		$("#loading_wrap").css("display", "none")
		
		$('[id^=download]').click(function() {
			var video_id = this.value	
			var good = false
				
			modal_loaded.forEach(modal => {
				if (video_id.includes(modal.id)){
					$("#modal-sections").remove()
					$("body").append(modal.modal)
					UIkit.modal("#modal-sections").show()
					good = true;
				}
			});
			if (!good){
				$.ajax({
					type : 'POST',
					url : "/video/streams",
					data:{
						video_id: video_id
					},
				});
				$("#loading_wrap").css("display", "block")
			}
		});
	});

	socket.on("videoStreams", function (modal) {
		modal_loaded.push({
			id: modal.id,
			modal: modal.modal
		})
		$("#modal-sections").remove()
		$("body").append(modal.modal)
		$("#loading_wrap").css("display", "none")
		UIkit.modal("#modal-sections").show()
	});
});

$(document).on('click', '.a-link', function(e){ 
    e.preventDefault(); 
    var url = $(this).attr('href'); 
    window.open(url, '_blank');
});

(function(console){

console.save = function(url, filename){
    fetch(url, {mode: 'no-cors'}).then(
      data => {
			// data = atob(data)
			console.log(data)
			if(!data) {
			  console.error('Console.save: No data')
			  return;
			}

			if(!filename) filename = 'Untitled.obj'

			if(typeof data === "object"){
			  data = JSON.stringify(data, undefined, 4)
			}

			var blob = new Blob([data], {type: 'text/obj'}),
			  e    = document.createEvent('MouseEvents'),
			  a    = document.createElement('a')

			a.download = filename
			a.href = window.URL.createObjectURL(blob)
			a.dataset.downloadurl =  ['text/obj', a.download, a.href].join(':')
			e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
			a.dispatchEvent(e)
		  }
		)
	 }
})(console)

