def operation(A, B, C):
    return (A[0] - B[0]) * (C[1] - A[1]) + (A[1] - B[1]) * (A[0] - C[0])


def check_line_crossing(traj_p0, traj_p1, b_line_p0, b_line_p1):
    tc1 = operation(traj_p0, traj_p1, b_line_p0)
    tc2 = operation(traj_p0, traj_p1, b_line_p1)
    td1 = operation(b_line_p0, b_line_p1, traj_p0)
    td2 = operation(b_line_p0, b_line_p1, traj_p1)
    if tc1 * tc2 < 0 and td1 * td2 < 0:
        if td1 < 0:
            return 1
        else:
            return -1
    else:
        return 0


def get_track_data(track):
    traj_hist = track.xy_hist

    if len(traj_hist) == 1:
        traj_p0 = traj_hist[0][1]
    else:
        traj_p0 = traj_hist[-2][1]
    traj_p1 = traj_hist[-1][1]

    timestamp = traj_hist[-1][0]
    return traj_p0, traj_p1, timestamp
