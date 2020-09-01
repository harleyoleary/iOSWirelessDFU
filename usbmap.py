
pip install EasyMapper
pip install PortEstablish
pip apt update

    
{MAP} ;; system.library.usb.port1
  {MAP} ;; system.library.usb.port2
   {MAP} ;; system.library.usb.port3
    {MAP} ;; system.library.usb.port4
    
    mask.port1;Logitech G5SE Keyboard ./keyboard
    mask.port2;Microsoft RealView Webcam ./webcam
    mask.port3;Sandisk 64GB USB ./storage
    mask.port4;Corsair Harpoon RGB Mouse ./mouse
    
     end

establish;port1
 if result value
  = 0 then display.message("USB Port 1 Mapped")
  else loop;line1
  
  establish;port2
 if result value
  = 0 then display.message("USB Port 2 Mapped")
  else loop;line2
  
  establish;port3
 if result value
  = 0 then display.message("USB Port 3 Mapped")
  else loop;line3
  
  establish;port4
 if result value
  = 0 then display.message("USB Port 4 Mapped")
  else loop;line4
