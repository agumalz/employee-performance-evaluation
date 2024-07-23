from django.http import HttpResponseForbidden

def fuzzy_membership(value, category):
    if category == 'rendah':
        if value <= 50:
            return 1
        elif 50 < value <= 75:
            return (75 - value) / 25
        else:
            return 0
    elif category == 'sedang':
        if 50 < value <= 75:
            return (value - 50) / 25
        elif 75 < value <= 100:
            return (100 - value) / 25
        else:
            return 0
    elif category == 'tinggi':
        if value <= 75:
            return 0
        elif 75 < value <= 100:
            return (value - 75) / 25
        else:
            return 1

def defuzzification(k1, k2, k3):
    rendah_k1 = fuzzy_membership(k1, 'rendah')
    sedang_k1 = fuzzy_membership(k1, 'sedang')
    tinggi_k1 = fuzzy_membership(k1, 'tinggi')

    rendah_k2 = fuzzy_membership(k2, 'rendah')
    sedang_k2 = fuzzy_membership(k2, 'sedang')
    tinggi_k2 = fuzzy_membership(k2, 'tinggi')

    rendah_k3 = fuzzy_membership(k3, 'rendah')
    sedang_k3 = fuzzy_membership(k3, 'sedang')
    tinggi_k3 = fuzzy_membership(k3, 'tinggi')

    z_k1 = (rendah_k1 * 50 + sedang_k1 * 75 + tinggi_k1 * 100) / (rendah_k1 + sedang_k1 + tinggi_k1)
    z_k2 = (rendah_k2 * 50 + sedang_k2 * 75 + tinggi_k2 * 100) / (rendah_k2 + sedang_k2 + tinggi_k2)
    z_k3 = (rendah_k3 * 50 + sedang_k3 * 75 + tinggi_k3 * 100) / (rendah_k3 + sedang_k3 + tinggi_k3)

    return z_k1, z_k2, z_k3

def normalization(defuzzified_values):
    max_values = [max(col) for col in zip(*defuzzified_values)]
    normalized_values = [[value / max_value for value, max_value in zip(row, max_values)] for row in defuzzified_values]
    return normalized_values

def saw(normalized_values, weights):
    preferences = [sum(val * weight for val, weight in zip(row, weights)) for row in normalized_values]
    return preferences

def crew_forbidden(request):
    if request.user.profile.position == 'crew':
        return HttpResponseForbidden("Anda tidak memiliki akses ke halaman ini.")
