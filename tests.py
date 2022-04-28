"""Testsq for Balloonicorn's Flask app."""

import unittest
import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn(b"having a party", result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        # FIXME: Add a test to show we haven't RSVP'd yet
        result = self.client.get("/")
        #test that we see the RSVP form 
        self.assertIn(b"Please RSVP", result.data)
        #test that we DON'T see party details
        self.assertNotIn(b"Treats", result.data)

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        # FIXME: check that once we log in we see party details--but not the form!
        self.assertNotIn(b"Please RSVP", result.data)
        self.assertIn(b"Treats", result.data)

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # # FIXME: write a test that mel can't invite himself
        # rsvp_info = {'name': "Mel", 'email': "mel@ubermelon.com"}
        # result = self.client.post("/rsvp", data=rsvp_info,
        #                           follow_redirects=True)
        # self.assertIn(b"Sorry, Mel", result.data)


        # rsvp_info2 = {'name': "Mel melitpolski", 'email': "mel@ubermelon.com"}
        # result2 = self.client.post("/rsvp", data=rsvp_info2,
        #                           follow_redirects=True)
        # self.assertIn(b"Sorry, Mel", result2.data)

        # rsvp_info3 = {'name': "Mel Melitpolski", 'email': "MEL@UBERMELON.COM"}
        # result3 = self.client.post("/rsvp", data=rsvp_info3,
        #                           follow_redirects=True)
        # self.assertIn(b"Sorry, Mel", result3.data) 

        # rsvp_info4 = {'name': "mel melitpolski", 'email': "Mel@ubermelon.com"}
        # result4 = self.client.post("/rsvp", data=rsvp_info4,
        #                           follow_redirects=True)
        # self.assertIn(b"Sorry, Mel", result4.data)      

        rsvp_infos =[{'name': "Mel", 'email': "mel@ubermelon.com"},
        {'name': "Mel melitpolski", 'email': "mel@ubermelon.com"},
        {'name': "Mel Melitpolski", 'email': "MEL@UBERMELON.COM"},
        {'name': "mel melitpolski", 'email': "Mel@ubermelon.com"}
        ]
        for rsvp in rsvp_infos:
            result = self.client.post("/rsvp", data=rsvp, follow_redirects=True)
            self.assertIn(b"Sorry, Mel", result.data)
                                
        # self.assertIn(b"Sorry, Mel", result.data)
        # self.assertIn(b"Mel@ubermelon.com", result.data)
        # self.assertIn(b"Mel melitpolski", result.data)
        # self.assertIn(b"MEL@UBERMELON.COM", result.data)


if __name__ == "__main__":
    unittest.main()
