def main(): 
    spacecraft = {"name": "James webb space Telescope", "distance": 163}
    spacecraft.update({"days": 54, "orbit": "Sun"})
    print(create_report(spacecraft))
    
def  create_report(spacecraft):
    return f""""
    ======= REPORT =======
    
    Name: {spacecraft["name"]}
    Distance: {spacecraft.get("distance", "unknown")} AU
    Days: {spacecraft.get("days", "unknown")}
    Orbit: {spacecraft.get("orbit", "unknown")}
    
    =======================
    """
main()
