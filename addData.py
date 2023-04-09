import firebase_admin
from firebase_admin import credentials, firestore

# import firebase_admin
# from firebase_admin import credentials
#
# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)


class AddData:
    def storedata(self):
        cred = credentials.Certificate("riderDataDetails.json")
        firebase_admin.initialize_app(cred)

        db = firestore.client()

        doc_ref = db.collection('users').document('user_001')
        doc_ref.set({
            'dlcard': 'imageURL',
            'name': 'string',
            'registeredImage': 'imageURL'
            # 'capImg': 'imgurl'
            # 'dateTime': 'April 4, 2023 at 10:35:37 AM UTC+5:30'
            # 'fine_amt': '500'
            # 'licNo': 'x01'
            # 'password': 'password'
            # 'paymentStatus': 'true'
            # 'review_status': 'false'


        })
