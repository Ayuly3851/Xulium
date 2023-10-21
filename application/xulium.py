from flask import render_template, Blueprint, request, flash, redirect, url_for, stream_template
from .utils.enum import VideoInfo, PlaylistInfo
from pytube import YouTube, Playlist, Search
from .utils.handle import Handle
from application import socketio
from .utils.timer import Timer
import re

xulium = Blueprint(name="xulium", import_name=__name__)

@xulium.route('/')
def index():
	return stream_template("index.html")

@xulium.route('/video', methods=["POST"])
def video():
	query = request.form.get("query")

	youtube_playlist_regex = re.compile('^https?:\/\/(www.youtube.com|youtube.com)\/playlist\?list=[A-z0-9-_]{34}')
	youtube_video_regex = re.compile('(?:https?:\/\/)?(?:youtu\.be\/|(?:www\.|m\.)?youtube\.com\/(?:watch|v|embed|shorts)(?:\.php)?(?:\?.*v=|\/))([a-zA-Z0-9\_-]+)')

	videos = []

	if youtube_playlist_regex.match(query):
		playlist = Playlist(query)
		for _, video in enumerate(playlist.videos):
			videoInfo = Handle.create_video_info(video)	
				
			html_code = Handle.card_video_html(videoInfo, _)
					
			videos.append(html_code)

	elif youtube_video_regex.match(query):
		video = YouTube(query)

		videoInfo = Handle.create_video_info(video)

		html_code = Handle.card_video_html(videoInfo, 0)

		videos.append(html_code)

	else:
		search_results = Search(query).results
		for _, video in enumerate(search_results):

			videoInfo = Handle.create_video_info(video)	
				
			html_code = Handle.card_video_html(videoInfo, _)
					
			videos.append(html_code)

	socketio.emit('updateVideos', {'videos': videos})

	return {'code': 0}

@xulium.route('/video/streams', methods=["POST"])
def video_streams():
	video_id = request.form.get("video_id")

	video = YouTube(f"https://www.youtube.com/watch?v={video_id}")

	streams = []

	for stream in video.streams:
		_stream = {}
		
		_stream["ext"] = stream.mime_type.split("/")[1]
		_stream["type"] = stream.type
		_stream["mime_type"] = stream.mime_type
		_stream["url"] = stream.url
		_stream["resolution"] = stream.resolution
		_stream["abr"] = stream.abr
		_stream["file_size_mb"] = f"{stream.filesize_mb} MB"

		streams.append(_stream)

	modal = Handle.download_modal_html(streams, video.title)

	socketio.emit('videoStreams', {'modal': modal, 'id': video.video_id})

	# return {'videoStreams', {'modal': modal, 'id': video.video_id}}
	return {'code': 0}

@xulium.route("/get_file_data")
def get_file_data():

	url_file = request.form.get("url_file")

	

"""
Decorator for connect
"""
@socketio.on('connect')
def connect():
	print('Client connected')

"""
Decorator for disconnect
"""
@socketio.on('disconnect')
def disconnect():
	print('Client disconnected',  request.sid)


