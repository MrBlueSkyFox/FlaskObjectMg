Current API

{base_url}/object_mgr - route to api for managment pool of objects
{base_url}/object_mgr}/set_object_pool - set up object pool send ["objects_number"] to define maximum size of pool
{base_url}/object_mgr}/get_object - get random free object from pool, return obj dict
{base_url}/object_mgr}/free_object/<obj_val> - free object, pass obj value

also added handle exception for wrong free params
for api docs it's bets to use Swagger or similar tools

for running demo
clone repo
run setup_container.sh
or bash setup_container.sh (if you using wsl)

flask running on port 8000