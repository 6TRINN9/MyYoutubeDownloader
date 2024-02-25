import flet as ft
import moviepy as mv
from pytube import YouTube

def main(page:ft.Page):    
    page.appbar=ft.AppBar(        
        actions=[
            ft.IconButton(ft.icons.GARAGE_SHARP),
        ],
    )
    
    page.bgcolor = ft.colors.WHITE 
    
        
    def textChanged(e):        
        try:
            video_details=YouTube(e.control.value)
            button.text = 'Download - '+ video_details.title      
            button.update()
            image.src = video_details.thumbnail_url
            image.update()      
        except:
            button.text = 'Download'     
            button.update()    
            image.src = ".\image\MyYoutubeLogo.png"
            image.update()  
            
    def downloadFile(e): 
        if len(txt.value) == 0:
            page.snack_bar=ft.SnackBar(ft.Text('Empty link', color=ft.colors.RED), bgcolor=ft.colors.BLACK38) 
            page.snack_bar.open = True
            page.update()
        else:
            try:
                get_link = txt.value
                video = YouTube(get_link).streams.get_highest_resolution().download()
                vid_clip = mv.editor.VideoFileClip(video)
                vid_clip.close
            except:
                page.snack_bar=ft.SnackBar(ft.Text('Not a youtube link or error', color=ft.colors.RED), bgcolor=ft.colors.BLACK38)
                page.snack_bar.open = True
                page.update()           
                
    txt = ft.TextField(hint_text='Link', on_change=textChanged)
    image = ft.Image(src=".\image\MyYoutubeLogo.png", width=200, fit=ft.ImageFit.COVER)
    button = ft.ElevatedButton('Download', on_click= downloadFile)
    
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER   
   
    page.add(
        image,
        ft.Container(height=7),
        txt,
        button
    )
    
ft.app(target=main)
