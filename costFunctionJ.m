function J = costFunctionJ(X, Y, theta)

% X is the "design matrix" containing our training examples
% y is the class labels

m = size(X, 1);             % size of X, row
predictions = X * theta;    % prediction of hypothesis on all m
                            % examples
sqrErrors = (predictions - Y) .^ 2; % squared errors

J = 1 / (2 * m) * sum(sqrErrors);
