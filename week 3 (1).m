totalSum = 0;  % Initialize the accumulator

for i = 1:100
    totalSum = totalSum + i;  % Add each number to the accumulator
end

disp(['The sum from 1 to 100 is: ', num2str(totalSum)]);