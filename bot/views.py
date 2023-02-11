from rest_framework import  generics, permissions, status
from rest_framework.response import  Response
from bot.models import TgUser
from bot.serializers import TgUserSerializer
from bot.telebot import send_message

HELP_COMMAND = """
список команд \n
/help - список команд \n
/goals - открытые цели \n
"""

class VerificationViews(generics.GenericAPIView):
    model = TgUser
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TgUserSerializer

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tguser = TgUser.objects.filter(verification_code=request.data['verification_code'])

        if len(tguser) > 0:
            if not tguser[0].verification_True:
                tguser[0].user_id = request.user.id
                tguser[0].verification_True = True
                tguser[0].save()
                strrez = "verification has been completed \n"
                strrez = strrez + f"добро пожаловать на борт {request.user.username} - {tguser[0].user_id } \n"
                strrez = strrez + HELP_COMMAND
                send_message(tguser[0].tg_id, strrez )
            else:
                send_message(tguser[0].tg_id, f"ты уже на борту {request.user.username} - {tguser[0].user_id }")
            data = {
                "tg_id": tguser[0].tg_id,
                "username": tguser[0].username,
                "verification_code": tguser[0].verification_code,
                "user_id": tguser[0].user_id
            }

        else:
            data = {
              "error" :  "verification_code not"
            }

        return Response(data , status=status.HTTP_200_OK)
