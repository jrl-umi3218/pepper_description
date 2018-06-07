#include <mc_rbdyn/RobotLoader.h>
#include <vrep-api-wrapper/vrep.h>
#include <cmath>

int main(int argc, char * argv[])
{
  double p = 1.0;
  double d = 0.0;
  if(argc > 1)
  {
    p = std::atof(argv[1]);
    if(argc > 2)
    {
      d = std::atof(argv[2]);
    }
  }
  auto rm = mc_rbdyn::RobotLoader::get_robot_module("pepper_ffb");
  vrep::VREP vrep;
  for(const auto & j : rm->mb.joints())
  {
    vrep.setJointPID(j.name(), p, 0, d);
  }
  return 0;
}
