class Mapper(object):

    def map(self, input):
        raise NotImplementedError

    def get_num_records(self):
        raise NotImplementedError

    def get_num_calls(self):
        raise NotImplementedError


class Filter(Mapper):
    """The top-most FilterClass class that defines the interface for input.

    You need to implement the filter() method and also keep the statistics up-to-date.
    """

    __num_records = 0
    __num_calls = 0

    def map(self, input):
        self.__num_calls += 1
        record = self.filter(input)

        if record is not None:
            self.__num_records += 1

        return record

    def filter(self, input):
        raise NotImplementedError

    def get_num_calls(self):
        """ Return the number of records this filter has produced. """
        return self.__num_calls

    def get_num_records(self):
        """ Return the number of times this filter has been called. """
        return self.__num_records


class RatingFilter(Filter):
    """Example of a RatingFilter that does nothing at the moment.

    Your task is to finish the initialiser, so that the range of film IDs can be configured,
    and to implement the filter method so that all ratings of films in the search range are filtered.
    The filter method shall return a tuple in the form of (key, value) pair
    with film ID as key and rating as value for further processing by our MR-simulator.
    """
    min_film_id = 0
    max_film_id = 0

    def __init__(self, start_movieid, end_movieid):
        # TODO
        self.min_film_id = int(start_movieid)
        self.max_film_id = int(end_movieid)

    def filter(self, line):
        # TODO
        attribs = line.split()
        if(len(attribs)==4):
            if(int(attribs[2]) in range(1,6) and int(attribs[1]) in range(self.min_film_id, self.max_film_id+1)):
                return (attribs[1], attribs[2])
            else:
                return None
        else:
            return None
            
