from .enum import VideoInfo
from .timer import Timer

class Handle:

	@staticmethod
	def card_video_html(videoInfo, _id):
		html_code = f"""
		  <div>
			  <div class="uk-card uk-border-rounded uk-card-secondary uk-box-shadow-hover-xlarge uk-card-body uk-dark uk-card-small">
				  <div class="uk-card-media-top">
					  <a href="{videoInfo.watch_url}" class="a-link">
						  <img class="uk-border-rounded" src="{videoInfo.thumbnail_url}" width="1800" height="1200" alt="">
					  </a>
				  </div>
				  <div class="uk-card-body" >
					  <h3 class="uk-card-title"><a class="text-link uk-link-heading a-link" onmouseover="this.style.color='#009acd'" onmouseout="this.style.color='#fff'" href="{videoInfo.watch_url}">{videoInfo.title}</a></h3>
					  <p>
						<span style="background-color: #0b66b5; color: #fff; font-family: 'proxima_nova_rgregular', helvetica, arial, sans-serif;" class="uk-label"><span uk-icon="icon: user; ratio: 0.7"></span> author</span> <a href="{videoInfo.channel_url}" class="uk-link-heading" onmouseover="this.style.color='#009acd'" onmouseout="this.style.color='#fff'">{videoInfo.author}</a>
					  </p>
					  <p><span uk-icon="icon: clock; ratio: 0.8"></span> Duration: <span style="background-color: #0b66b5; color: #fff !important; " class="uk-badge">{videoInfo.duration}</span></p>
					  <p><span uk-icon="icon: eye; ratio: 0.8"></span> Views: <span style="background-color: #0b66b5; color: #fff !important" class="uk-badge">{videoInfo.views}</span></p>
					  <div class="uk-dark" uk-margin>
						  <button value="{videoInfo.video_id}" id="download{_id}" class="uk-button uk-border-rounded uk-width-1-1 uk-dark uk-button-primary" style="background-color: #1c7ed6; color: #fff" onmouseover="this.style.backgroundColor='#1864ab'" onmouseout="this.style.backgroundColor='#1c7ed6'"><span uk-icon="icon: download"></span> Download</button>
					  </div>
				  </div>
			  </div>
		  </div>
		"""

		return html_code

	@staticmethod
	def download_modal_html(streams, video_title):
		videos = ""
		audios = ""

		for stream in streams:
			if stream["type"] == "video":
				videos += f"""
				<tr>
					<td>{stream["resolution"]}</td>
					<td><span style="background-color: #0b66b5; color: #fff; font-family: 'proxima_nova_rgregular', helvetica, arial, sans-serif;" class="uk-label">{stream["mime_type"]}</span></td>
					<td><span style="background-color: #0b66b5; color: #fff; font-family: 'proxima_nova_rgregular', helvetica, arial, sans-serif;" class="uk-label">{stream["file_size_mb"]}</span></td>
					<td><a href="{stream["url"]}" class="uk-button uk-border-rounded uk-dark uk-button-primary a-link" style="background-color: #1c7ed6; color: #fff" onmouseover="this.style.backgroundColor='#1864ab'" onmouseout="this.style.backgroundColor='#1c7ed6'" rel="nofollow"><span uk-icon="icon: download" ></span></a></td>
				</tr>
				"""

			elif stream["type"] == "audio":
				audios += f"""
				<tr>
					<td>{stream["abr"]}</td>
					<td><span style="background-color: #0b66b5; color: #fff; font-family: 'proxima_nova_rgregular', helvetica, arial, sans-serif;" class="uk-label">{stream["mime_type"]}</span></td>
					<td><span style="background-color: #0b66b5; color: #fff; font-family: 'proxima_nova_rgregular', helvetica, arial, sans-serif;" class="uk-label">{stream["file_size_mb"]}</span></td>
					<td><a href="{stream["url"]}" class="uk-button uk-border-rounded uk-dark uk-button-primary a-link" style="background-color: #1c7ed6; color: #fff; height: 40px" onmouseover="this.style.backgroundColor='#1864ab'" onmouseout="this.style.backgroundColor='#1c7ed6'" rel="nofollow"><span uk-icon="icon: download"></span></a></td>
				</tr>
				"""

		html_code = f"""
<div id="modal-sections" class="uk-dark" uk-modal>
    <div class="uk-modal-dialog uk-modal-body uk-border-rounded" uk-overflow-auto>
        <button class="uk-modal-close-default" type="button" uk-close></button>
		<h2 class="uk-modal-title">Download</h2>
        <div class="">
            <ul uk-tab="animation: uk-animation-slide-left-medium, uk-animation-slide-right-medium">
				<li><a>Video</a></li>
				<li><a>Audio</a></li>
			</ul>

			<ul class="uk-switcher uk-margin">
				<li>
					<table class="uk-table uk-table-justify uk-table-divider">
						<thead>
							<tr>
								<th class="uk-width-small">Resolution</th>
								<th>Mime Type</th>
								<th>File Size</th>
								<th>Action</th>	
							</tr>
						</thead>
						<tbody>
							{videos}
						</tbody>
					</table>
				</li>

				<li>
					<table class="uk-table uk-table-justify uk-table-divider">
						<thead>
							<tr>
								<th class="uk-width-small">Abr</th>
								<th>Mime Type</th>
								<th>File Size</th>
								<th>Action</th>	
							</tr>
						</thead>
						<tbody>
							{audios}
						</tbody>
					</table>
				</li>
			</ul>
        </div>
    </div>
</div>	
		"""

		return html_code

	@staticmethod
	def convert_number_to_abbreviated_format(number):

		suffixes = ['', 'K', 'M', 'B', 'T']
		suffix_index = 0

		while number >= 1000 and suffix_index < len(suffixes) - 1:
			number /= 1000
			suffix_index += 1

		return f'{number:.0f}{suffixes[suffix_index]}'

	@staticmethod
	def create_video_info(video):
		videoInfo = VideoInfo()
			
		videoInfo.title = video.title
		videoInfo.thumbnail_url = video.thumbnail_url
		videoInfo.watch_url = video.watch_url
		videoInfo.author = video.author
		videoInfo.duration = Timer.format(video.length)
		videoInfo.video_id = video.video_id
		videoInfo.views = Handle.convert_number_to_abbreviated_format(video.views)
		videoInfo.channel_url = video.channel_url

		return videoInfo
