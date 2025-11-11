def bandingkan_dengan_rata(total_user, rata_nasional=2500):
    selisih = total_user - rata_nasional
    persen = abs(selisih) / rata_nasional * 100
    if selisih > 0:
        return "di atas rata-rata Indonesia", persen
    else:
        return "di bawah rata-rata Indonesia", persen
