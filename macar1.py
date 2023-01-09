import math

points1 = [    (1, 2, 3),    (4, 5, 6),    (7, 8, 9),    (10, 11, 12),    (13, 14, 15)]

points2 = [    (16, 17, 18),    (19, 20, 21),    (22, 23, 24),    (25, 26, 27),    (28, 29, 30)]


def match(graph, match_from, match_to, matched):
    # Eğer grafın hiçbir üyesine eşleştirilemediysek, eşleştirmeyi döndür
    if match_from == len(graph):
        return matched

    # İlgili üyeye ait eşleştirmeyi dene
    for to in match_to:
        if (match_from, to) not in matched and (to, match_from) not in matched:
            # Eğer başarılı ise, bu eşleştirmeyi eşleştirilenler listesine ekle
            matched.append((match_from, to))
            # Bir sonraki üyeye geç ve bu üyenin eşleştirilebilir üyelerini dene
            result = match(graph, match_from + 1, match_to, matched)
            if result is not None:
                if result is not None:
                    return result
                # Eğer bu eşleştirme başarısız ise, eşleştirilenler listesinden kaldır
                matched.pop()
                # Eğer hiçbir eşleştirme başarılı olamadıysa, None döndür
            return None


def distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)


def match_points(points1, points2):
    # Graf üyelerini oluştur: her bir nokta, diğer noktalarla eşleştirilebilir
    graph = [(i, j) for i in range(len(points1)) for j in range(len(points2))]

    # Tüm graf üyelerini dolaş ve her üyenin eşleştirilebilir üyelerine bir eşleştirme oluşturmaya çalış
    matched = match(graph, 0, range(len(points2)), [])

    # Eşleştirilen noktaları döndür
    return [(points1[i], points2[j]) for (i, j) in matched if i < len(points1) and j < len(points2)]


matched = match_points(points1, points2)

print(matched)