echo "
!/usr/bin/env python
coding: utf-8

Lab:    WUME Lab, Lehigh Unviersity
Author: Eashan Adhikarla

This script collect images every n-th/400-th seconds from webcams which does not provide webcam links.
Note: Press Ctrl+D to stop the script.

Get the youtube links by; 
youtube-dl -g 'youtube_url'
"

newdirname=$(awk -F"," '{print $1}' webcam-list.csv)
if [ -d "$newdirname" ]; then
echo -e "Directory already exists" ;
else
`mkdir -p $newdirname`;
echo -e "\n$newdirname\n\n---All directories are created---\n"
fi

N="1"
while :
do

	###############################################################################
	# OTHERS
	###############################################################################
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://www.coloradowebcam.net/webcam/aspensq02/current.jpg' -frames:v 1 $(awk -F "," 'NR==11{print $1}' webcam-list.csv)/pool_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://www.coloradowebcam.net/webcam/aspensq03/current.jpg' -frames:v 1 $(awk -F "," 'NR==12{print $1}' webcam-list.csv)/hotel_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://www.coloradowebcam.net/webcam/aspensq04/current.jpg' -frames:v 1 $(awk -F "," 'NR==13{print $1}' webcam-list.csv)/gondola_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'http://coupevilleweather.us/webcam/weathercam.jpg' $(awk -F "," 'NR==14{print $1}' webcam-list.csv)/weathercam_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://2ganwc3heo6y2kcytm13s0hf-wpengine.netdna-ssl.com/wp-content/dialup/frontstreet.jpg' -frames:v 1 $(awk -F "," 'NR==15{print $1}' webcam-list.csv)/frontstreet_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://2ganwc3heo6y2kcytm13s0hf-wpengine.netdna-ssl.com/wp-content/dialup/festhalle.jpg' -frames:v 1 $(awk -F "," 'NR==16{print $1}' webcam-list.csv)/festhalle_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://2ganwc3heo6y2kcytm13s0hf-wpengine.netdna-ssl.com/wp-content/dialup/promenade1.jpg' -frames:v 1 $(awk -F "," 'NR==17{print $1}' webcam-list.csv)/promenade_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'http://24.73.111.162/mjpg/video.mjpg' -frames:v 1 $(awk -F "," 'NR==18{print $1}' webcam-list.csv)/bezach_$N.png # Florida Beach
	# ffmpeg -loglevel warning -hide_banner -stats -i 'http://162.17.248.193:81/mjpg/video.mjpg' -frames:v 1 $(awk -F "," 'NR==19{print $1}' webcam-list.csv)/cherryhills_$N.png # Cherry Hills, New Jersey
	# ffmpeg -loglevel warning -hide_banner -stats -i 'http://camera.clemson.edu/core2/fullsize.jpg' -frames:v 1 $(awk -F "," 'NR==20{print $1}' webcam-list.csv)/clemsoncampus_$N.png # Clemson University Core Campus
	# ffmpeg -loglevel warning -hide_banner -stats -i 'http://www.washington.edu/cambots/camera4_l.jpg' -frames:v 1 $(awk -F "," 'NR==21{print $1}' webcam-list.csv)/walsh_$N.png # Walsh Gardner Tacoma Webcam,WA
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://live1.brownrice.com/cam-images/westland.jpg' -frames:v 1 $(awk -F "," 'NR==36{print $1}' webcam-list.csv)/venice_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://www.redlodge.com/webcam_BD/camera0.jpg' -frames:v 1 $(awk -F "," 'NR==37{print $1}' webcam-list.csv)/redlodge_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'http://96.70.185.14:81/axis-cgi/mjpg/video.cgi?resolution=704x480&dummy=1360360695556' -frames:v 1 $(awk -F "," 'NR==44{print $1}' webcam-list.csv)/fishers_popcorn_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://www.nps.gov/webcams-glac/apvccam.jpg' -frames:v 1 $(awk -F "," 'NR==48{print $1}' webcam-list.csv)/apgar_village_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://www.skigd.com/webcam/webcam.jpg' -frames:v 1 $(awk -F "," 'NR==49{print $1}' webcam-list.csv)/great_divide_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'http://www.fortbentonwebcam.com/FTBenton13th.jpg' -frames:v 1 $(awk -F "," 'NR==52{print $1}' webcam-list.csv)/fort_benton_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'http://www.fortbentonwebcam.com/FTBentonFTStreet.jpg' -frames:v 1 $(awk -F "," 'NR==53{print $1}' webcam-list.csv)/St_front_benton_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'http://clearwaterwebcams.com/bigfork.php' -frames:v 1 $(awk -F "," 'NR==54{print $1}' webcam-list.csv)/montana_properties_$N.png
	# ffmpeg -loglevel warning -hide_banner -stats -i 'http://199.111.154.127:8080/cam_1.cgi#.X3nlvDpxxWw.link' -frames:v 1 $(awk -F "," 'NR==63{print $1}' webcam-list.csv)/virginia_$N.png # Virginia
	# ffmpeg -loglevel warning -hide_banner -stats -i 'http://162.17.212.89:8000/mjpg/video.mjpg#.X3noFkAaQhs.link' -frames:v 1 $(awk -F "," 'NR==64{print $1}' webcam-list.csv)/washington_$N.png # District Of Columbia, Washington DC
	# ffmpeg -loglevel warning -hide_banner -stats -i 'http://24.62.102.34:8080/mjpg/video.mjpg#.X3np2qc4Jc0.link' -frames:v 1 $(awk -F "," 'NR==65{print $1}' webcam-list.csv)/maynard_$N.png # Maynard, Massachusetts
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://livecam-static.olemiss.edu/raisingcanes.jpg?' -frames:v 1 $(awk -F "," 'NR==66{print $1}' webcam-list.csv)/tampa_$N.png # University of Tampa
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://livecam-static.olemiss.edu/unioncafe.jpg?' -frames:v 1 $(awk -F "," 'NR==67{print $1}' webcam-list.csv)/tampa_cafe_$N.png # University of Tampa - Union Cafe 
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://livecam-static.olemiss.edu/steakandshake.jpg?' -frames:v 1 $(awk -F "," 'NR==68{print $1}' webcam-list.csv)/steakandshake_$N.png # University of Tampa - Steak n' Shake
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://livecam-static.olemiss.edu/einsteinatanderson.jpg?' -frames:v 1 $(awk -F "," 'NR==69{print $1}' webcam-list.csv)/einsteinatanderson_$N.png # University of Tampa - Einstein Bros Bagels
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://livecam-static.olemiss.edu/starbucks.jpg?' -frames:v 1 $(awk -F "," 'NR==70{print $1}' webcam-list.csv)/starbucks_$N.png # University of Tampa - Library - Starbucks
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://livecam-static.olemiss.edu/freshii.jpg?' -frames:v 1 $(awk -F "," 'NR==71{print $1}' webcam-list.csv)/freshii_$N.png # University of Tampa - Freshii
	# ffmpeg -loglevel warning -hide_banner -stats -i 'https://livecam-static.olemiss.edu/unionplaza.jpg?' -frames:v 1 $(awk -F "," 'NR==72{print $1}' webcam-list.csv)/unionplaza_$N.png # University of Tampa - Union Plaza


	ffmpeg -loglevel warning -hide_banner -stats -i 'https://s7.ipcamlive.com/streams/07wsd6bbsr82zz3lv/snapshot.jpg' -frames:v 1 $(awk -F "," 'NR==38{print $1}' webcam-list.csv)/punta_fishermen_$N.png # https://kingfisherfleet.com/live-cam/
	ffmpeg -loglevel warning -hide_banner -stats -i 'https://s26.ipcamlive.com/streams/1a3ausbycwiretv7g/snapshot.jpg' -frames:v 1 $(awk -F "," 'NR==38{print $1}' webcam-list.csv)/ocean_city_broadwalk_$N.png # https://oceancitylive.com/ocean-city-webcams/ocean-city-boardwalk-shark-eye-cam/
	ffmpeg -loglevel warning -hide_banner -stats -i 'https://s11.ipcamlive.com/streams/0bgqptfem2cidekno/snapshot.jpg' -frames:v 1 $(awk -F "," 'NR==39{print $1}' webcam-list.csv)/ocean_city_MD_broadwalk2_$N.png # https://oceancitylive.com/ocean-city-webcams/ocean-city-md-boardwalk-cam-2/
	ffmpeg -loglevel warning -hide_banner -stats -i 'https://s42.ipcamlive.com/streams/2a7hz0uxcswqtdrar/snapshot.jpg' -frames:v 1 $(awk -F "," 'NR==40{print $1}' webcam-list.csv)/thrashers_fries_$N.png # https://oceancitylive.com/ocean-city-webcams/thrashers-french-fries/
	ffmpeg -loglevel warning -hide_banner -stats -i 'https://s11.ipcamlive.com/streams/0bbwvqzvnzji94gao/snapshot.jpg' -frames:v 1 $(awk -F "," 'NR==41{print $1}' webcam-list.csv)/ocean_city_amusements_$N.png # https://oceancitylive.com/ocean-city-webcams/ocean-city-md-amusements-pier-cam/
	ffmpeg -loglevel warning -hide_banner -stats -i 'https://s11.ipcamlive.com/streams/0bagcmpjldp6bw8tm/snapshot.jpg' -frames:v 1 $(awk -F "," 'NR==42{print $1}' webcam-list.csv)/castle_sand_$N.png # https://oceancitylive.com/ocean-city-webcams/castle-in-the-sand/
	ffmpeg -loglevel warning -hide_banner -stats -i 'https://s47.ipcamlive.com/streams/2fukzbfkol5s61zhc/snapshot.jpg' -frames:v 1 $(awk -F "," 'NR==43{print $1}' webcam-list.csv)/mackys_bayside_$N.png # https://oceancitylive.com/ocean-city-webcams/ocean-city-boardwalk-cam/
	ffmpeg -loglevel warning -hide_banner -stats -i 'https://s50.ipcamlive.com/streams/32ixdl4i3d1urs20t/snapshot.jpg' -frames:v 1 $(awk -F "," 'NR==47{print $1}' webcam-list.csv)/maryland_broadwalk_$N.png # https://oceancitylive.com/ocean-city-webcams/ocean-city-maryland-boardwalk-audio-cam/
	ffmpeg -loglevel warning -hide_banner -stats -i 'https://s50.ipcamlive.com/streams/32ixdl4i3d1urs20t/snapshot.jpg' -frames:v 1 $(awk -F "," 'NR==62{print $1}' webcam-list.csv)/maryland_broadwalk__$N.png # https://oceancitylive.com/ocean-city-webcams/ocean-city-maryland-boardwalk-audio-cam/

	###############################################################################
	# Earthcam
	###############################################################################
	# streamlink "https://www.earthcam.com/usa/florida/naples/?cam=naplespier" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==1{print $1}' webcam-list.csv)/naples_bay$N.png
	# streamlink "https://www.earthcam.com/usa/southcarolina/myrtlebeach/?cam=myrtlebeach_hd" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==2{print $1}' webcam-list.csv)/myrtle_beach_south$N.png
	# streamlink "https://www.earthcam.com/usa/southcarolina/myrtlebeach/?cam=myrtlebeach_hd2" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==3{print $1}' webcam-list.csv)/myrtle_beach_north$N.png
	# streamlink "https://www.earthcam.com/usa/louisiana/neworleans/bourbonstreet/?cam=bourbonstreet" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==4{print $1}' webcam-list.csv)/bourbon_street$N.png
	# streamlink "https://www.earthcam.com/usa/louisiana/neworleans/bourbonstreet/?cam=catsmeow2" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==5{print $1}' webcam-list.csv)/catsmeow2$N.png
	# streamlink "https://www.earthcam.com/usa/newjersey/seasideheights/?cam=seasideheights" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==6{print $1}' webcam-list.csv)/seasideheights$N.png
	# streamlink "https://www.earthcam.com/usa/newjersey/seasideheights/?cam=seasideheights2" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==7{print $1}' webcam-list.csv)/seasideheights2$N.png
	# streamlink "https://www.earthcam.com/usa/illinois/chicago/wrigleyville/?cam=wrigleyville" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==8{print $1}' webcam-list.csv)/wrigleyville$N.png
	# streamlink "https://www.earthcam.com/usa/illinois/chicago/wrigleyfield/?cam=wrigleyfield_hd" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==9{print $1}' webcam-list.csv)/wrigleyville_hd$N.png
	# streamlink "https://www.earthcam.com/usa/georgia/athens/?cam=athensga" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==10{print $1}' webcam-list.csv)/hotel_indigo_athens$N.png
	# streamlink "https://www.earthcam.com/usa/florida/lauderdalebythesea/town/?cam=lbts_town" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==31{print $1}' webcam-list.csv)/Lauderdale-By-The-Sea$N.png
	# streamlink "https://www.earthcam.com/usa/missouri/stlouis/?cam=arch_riverview" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==32{print $1}' webcam-list.csv)/St_Louis$N.png
	# streamlink "https://www.earthcam.com/usa/michigan/brighton/?cam=brighton" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==33{print $1}' webcam-list.csv)/brighton_michigan$N.png
	# streamlink "https://www.earthcam.com/usa/iowa/dyersville/?cam=dyersville" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==34{print $1}' webcam-list.csv)/dyersville_Iowa$N.png
	# streamlink "https://www.earthcam.com/usa/newmexico/lasvegas/?cam=lasvegasnm" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==45{print $1}' webcam-list.csv)/Historic_plaza_park$N.png
	# streamlink "https://www.earthcam.com/usa/newyork/littleitaly/?cam=littleitaly" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==62{print $1}' webcam-list.csv)/mulberry_street$N.png
	# streamlink "https://www.earthcam.com/usa/florida/miamiandthebeaches/?cam=miamibeach10" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==66{print $1}' webcam-list.csv)/miami$N.png
	# streamlink "https://www.earthcam.com/cams/florida/miami/?cam=miami" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==67{print $1}' webcam-list.csv)/news_cafe$N.png
	# streamlink "https://www.earthcam.com/usa/florida/keywest/?cam=irishkevins" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $(awk -F "," 'NR==68{print $1}' webcam-list.csv)/key_west$N.png
	
	# # streamlink "" best -O | ffmpeg -loglevel warning -hide_banner -stats -i pipe:0 -frames:v 1 $N.png
	
	###############################################################################
	# Youtube
	###############################################################################
	# # ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=mRe-514tGMg") -frames:v 4 $(awk -F "," 'NR==22{print $1}' webcam-list.csv)/times_square_%03d.png
	# # ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=7DVUvR_ic-M") -frames:v 4 $(awk -F "," 'NR==23{print $1}' webcam-list.csv)/church_street_%03d.png
	# ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=qP1y7Tdab7Y") -frames:v 4 $(awk -F "," 'NR==24{print $1}' webcam-list.csv)/watertown_%03d.png
	# ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=1EiC9bvVGnk") -frames:v 4 $(awk -F "," 'NR==25{print $1}' webcam-list.csv)/jackson_hole_%03d.png
	# # ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=AAYiFaPV8G4") -frames:v 4 $(awk -F "," 'NR==26{print $1}' webcam-list.csv)/port_huron_%03d.png
	# ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=DoUOrTJbIu4") -frames:v 4 $(awk -F "," 'NR==27{print $1}' webcam-list.csv)/jackson_town_%03d.png
	# ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=4qyZLflp-sI") -frames:v 4 $(awk -F "," 'NR==28{print $1}' webcam-list.csv)/1560_broadway_%03d.png
	# ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=Y_TLxje5Qw4") -frames:v 4 $(awk -F "," 'NR==29{print $1}' webcam-list.csv)/alpine_lodge_%03d.png
	# ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=hORCPr-jWhk") -frames:v 4 $(awk -F "," 'NR==30{print $1}' webcam-list.csv)/canmore_%03d.png
	# # ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=g7fWaol3P1g") -frames:v 4 $(awk -F "," 'NR==50{print $1}' webcam-list.csv)/grand_targhee_resort_%03d.png
	# # ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=2fLoP1AP9X0") -frames:v 4 $(awk -F "," 'NR==51{print $1}' webcam-list.csv)/grand_targhee_resort_plaza_%03d.png
	# # ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=bB96qObNTSU") -frames:v 4 $(awk -F "," 'NR==55{print $1}' webcam-list.csv)/tampa_%03d.png
	# ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=3XTcfrdVh6E") -frames:v 4 $(awk -F "," 'NR==56{print $1}' webcam-list.csv)/carmel_indiana_%03d.png
	# ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=5TxrAw72TcQ") -frames:v 4 $(awk -F "," 'NR==57{print $1}' webcam-list.csv)/carters_green_%03d.png
	# ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=6l5WCN5Re6k") -frames:v 4 $(awk -F "," 'NR==58{print $1}' webcam-list.csv)/seascape_whales_%03d.png
	# ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=WuhUkOvFMyA") -frames:v 4 $(awk -F "," 'NR==59{print $1}' webcam-list.csv)/sturgis_motorcycle_museum_%03d.png
	# ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=d66NPsy_MPg") -frames:v 4 $(awk -F "," 'NR==60{print $1}' webcam-list.csv)/sturgis_motorcycle_museum2_%03d.png
	# ffmpeg -loglevel warning -hide_banner -stats -i $(youtube-dl -g "https://www.youtube.com/watch?v=9IbruokZzx0") -frames:v 4 $(awk -F "," 'NR==61{print $1}' webcam-list.csv)/southampton_village_%03d.png

	sleep 400
	N=`expr $N + 1`
done
