from json_wrapper import JSon
from bs import BS
from shot_chart_line import SCLine


def print_shot_chart_data_from_team(data_team):
    for item in data_team:
        scl = SCLine(item)
        print(f"id. jugador: {scl.id} - anotado: {scl.scored} - txt: {scl.txt} - "
              f"home: {scl.home} - style: {item['style']} - x: {scl.x} - y:  {scl.y}")


def main():
    bs = BS("https://www.espn.com/nba/playbyplay/_/gameId/401332840")
    print("\n\nEQUIPO VISITANTE")
    print_shot_chart_data_from_team(bs.soup.find("ul", class_="shots away-team").find_all("li"))
    print("\n\nEQUIPO LOCAL")
    print_shot_chart_data_from_team(bs.soup.find("ul", class_="shots home-team").find_all("li"))
    print("\n\nPBP")
    json = JSon("https://livestats.dcd.shared.geniussports.com/data/1859912/data.json")
    print(json.json["pbp"])

    print("¡¡¡FIN PROCESO!!!")

main()
