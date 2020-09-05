from django.http import Http404, HttpResponseBadRequest
from rest_framework.decorators import api_view, action
from main.exceptions import BadSendPaymentRequest
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response

SUM = "sum"
TO = "to"
STATE = "state"
USER = "user"



class StateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class ManagerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


    @action(detail=False, methods=['post'])
    def about(self, request):
        if not USER in request.data.keys():
            raise BadSendPaymentRequest()
        try:
            person = Person.objects.get(user__username=request.data[USER])
            return Response(PersonSerializer(person).data)
        except:
            pass

        raise Http404()

    @action(detail=True, methods=['post'])
    def set_state(self, request, pk=None):

        """
         {
            "state": string,
        }
        """
        keys = request.data.keys()

        if not STATE in keys:
            raise BadSendPaymentRequest()
        state_name = request.data[STATE]
        try:
            person = Person.objects.get(id=pk)
            state = State.objects.get(name=state_name)
            person.states.add(state)
            person.save()
            return Response(PersonSerializer(person).data)
        except Exception as e:
            raise Http404(e)

    @action(detail=True, methods=['post'])
    def delete_state(self, request, pk=None):
        """
                 {
                    "state": string,
                }
                """
        keys = request.data.keys()

        if not STATE in keys:
            raise BadSendPaymentRequest()
        state_name = request.data[STATE]
        try:
            person = Person.objects.get(id=pk)
            state = State.objects.get(name=state_name)
            person.states.remove(state)
            person.save()
            return Response(PersonSerializer(person).data)
        except Exception as e:
            raise Http404(e)


class DocumentViewSet:
    pass


class PassportViewSet(DocumentViewSet, viewsets.ViewSet):

    def list(self, request):
        queryset = Passport.objects.all()
        serializer = PassportSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.objects.get(id=pk).passport
        try:
            serializer = PassportSerializer(queryset)
        except Exception as e:
            raise Http404(e)

        return Response(serializer.data)


class BloodViewSet(DocumentViewSet, viewsets.ViewSet):

    def list(self, request):
        queryset = Blood.objects.all()
        serializer = BloodSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.objects.get(id=pk).blood
        try:
            serializer = BloodSerializer(queryset)
        except Exception as e:
            raise Http404(e)

        return Response(serializer.data)


class FingetPrintViewSet(DocumentViewSet, viewsets.ViewSet):

    def list(self, request):
        queryset = FingerPrint.objects.all()
        serializer = FingerPrintSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.objects.get(id=pk).fingerprint
        try:
            serializer = FingerPrintSerializer(queryset)
        except Exception as e:
            raise Http404(e)

        return Response(serializer.data)


class GunViewSet(DocumentViewSet, viewsets.ViewSet):

    def list(self, request):
        queryset = GunDocument.objects.all()
        serializer = GunLicenceSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.objects.get(id=pk)
        try:
            serializer = PassportSerializer(queryset.passport)
        except Exception as e:
            raise Http404(e)

        return Response(serializer.data)


class DriversViewSet(DocumentViewSet, viewsets.ViewSet):

    def list(self, request):
        queryset = DriversLicence.objects.all()
        serializer = DriverLicenceSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.objects.get(id=pk).driverslicence
        try:
            serializer = DriverLicenceSerializer(queryset)
        except Exception as e:
            raise Http404(e)

        return Response(serializer.data)


class BankAccountViewSet(DocumentViewSet, viewsets.ViewSet):

    def list(self, request):
        queryset = BankAccount.objects.all()
        serializer = BankaccountSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Person.objects.get(id=pk).bankaccount
        try:
            serializer = BankaccountSerializer(queryset)
        except Exception as e:
            raise Http404(e)

        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def send_money(self, request, pk=None):

        """
         {
            "to": string,
            "sum": int
        }
        """
        keys = request.data.keys()

        if not SUM in keys and not TO in keys:
            raise BadSendPaymentRequest()

        try:
            person = Person.objects.get(id=pk)
            bank_account: BankAccount = person.bankaccount
            bank_account_for_send = BankAccount.objects.get(bank_account_number=request.data[TO])
            bank_account.balance = bank_account.balance - request.data[SUM]
            bank_account_for_send.balance = bank_account_for_send.balance + request.data[SUM]
            bank_account.save()
            bank_account_for_send.save()
            return Response(BankaccountSerializer(bank_account).data)

        except Exception as e:
            raise Http404(e)


class FriendsViewSet(DocumentViewSet, viewsets.ViewSet):

    def list(self, request):
        queryset = Friends.objects.all()
        serializer = FriendsSerializer(queryset, many=True)
        return Response(serializer.data)
