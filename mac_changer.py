import subprocess
import optparse

parse= optparse.OptionParser



interface= input('please enter the interface: ')
new_mac= input('please enter the new mac: ')

print('changing mac of '+interface+'to'+new_mac)

subprocess.call(['ifconfig',+interface+ 'down' ])
subprocess.call(['ifconfig',+interface+ 'hw', 'ether', +new_mac ])
subprocess.call(['ifconfig',+interface+ 'up' ])