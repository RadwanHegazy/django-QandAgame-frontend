from django.shortcuts import render, redirect
from globals.decorators import login_required
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.views import View
from django.contrib.messages import error

class GetRoom (View) : 

    @login_required
    def get(self, request, room_number, **kwargs) :
        context = {}

        action = Action(
            url=MAIN_URL + f"/game/room/get/{room_number}",
            headers=kwargs['headers']
        )


        action.get()
        
        if not action.is_valid:
            error(request, 'room not found')
            return redirect('profile')
        

        context = action.json_data()
        me_questions = context['me_questions']

        if int(me_questions) == 2:
            return redirect('start_room', room_number)
        
        return render(request, 'room.html',context)
    

    @login_required
    def post (self, request, room_number, **kwargs) :
        action = Action(
            url=MAIN_URL + f"/game/question/create/{room_number}",
            headers=kwargs['headers'],
            data={
                'text' : request.POST.get('text')
            }
        )

        action.post()

        return redirect('room', room_number)
    

class StartRoom (View) :

    @login_required
    def get(self, request, room_number, **kwargs) : 
        action = Action(
            url=MAIN_URL + f"/game/room/get/{room_number}",
            headers=kwargs['headers']
        )


        action.get()
        
        if not action.is_valid:
            error(request, 'room not found')
            return redirect('profile')
        
        return render(request, 'game.html',{
            'room_number' : room_number,
            'total_questions' : action.json_data()['total_questions'],
        })