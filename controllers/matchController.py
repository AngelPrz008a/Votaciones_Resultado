from repository.matchRepository import MatchRepository
from models.match import Match


class MatchController():

    def __init__(self):
        self.matchRepository = MatchRepository()

    def index(self):
        return self.matchRepository.findAll()

    def create(self, theMatch):
        newMatch = Match(theMatch)
        return self.matchRepository.save(newMatch)

    def show(self, id):
        theMatch = Match(self.matchRepository.findById(id))
        return theMatch.__dict__

    def update(self, id, theMatch):
        model = Match(theMatch)
        return self.matchRepository.update(id, model)

    def delete(self, id):
        return self.matchRepository.delete(id)
