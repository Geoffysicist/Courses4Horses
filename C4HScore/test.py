import c4h_scoreboard as c4h
import yaml

def test_event():
    event = c4h.C4HEvent("Great Event")
    print(type(event))
    fn = "test_out.c4hs"
    event.yaml_dump(fn)

    print('done')

def test_articles():
    fn = 'C4HScore\ea_articles.yaml'
    with open(fn, 'r') as in_file:
        articles = yaml.load(in_file, Loader=yaml.FullLoader)

    for a, b in articles.items():
        print(f'{a} {b}\n')

if __name__ == "__main__":
    test_articles()
    