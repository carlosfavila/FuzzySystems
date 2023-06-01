x=0:0.1:10;
A=x./(x+2);
B=2.^(-x);
C=1./(1+(10*(x-2).^2));

fig=figure(1);
subplot(3,3,1)
plot(x,A,'--r',x,B,'--k',x,max(A,B))
title("A v B")
xlabel("Universe")

subplot(3,3,2)
plot(x,A,'r',x,C,'g',x,max(A,C))
title("A v C")
xlabel("Universe")

subplot(3,3,3)
plot(x,B,'--k',x,C,'--g',x,max(B,C))
title("B v C")
xlabel("Universe")

subplot(3,3,4)
plot(x,A,'--r',x,B,'--k',x,min(A,B),'b')
title("A n B")
xlabel("Universe")

subplot(3,3,5)
xlabel("Universe")
plot(x,A,'--r',x,C,'--g',x,min(A,C),'b')
title("A n C")
xlabel("Universe")

subplot(3,3,6)
plot(x,B,'--k',x,C,'--g',x,min(B,C),'b')
title("B n C")
xlabel("Universe")

subplot(3,3,7)
plot(x,A,'--r',x,1-A,'m')
title("Complement of A")
xlabel("Universe")

subplot(3,3,8)
plot(x,B,'--k',x,1-B,'m')
title("Complement of B")
xlabel("Universe")

subplot(3,3,9)
plot(x,C,'--g',x,1-C,'m')
title("Complement of C")
xlabel("Universe")


han=axes(fig,'visible','off'); 
han.Title.Visible='on';
han.YLabel.Visible='on';
ylabel(han,"Membership Degree")
title(han, "Basic Operations");