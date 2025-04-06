import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = signUpUser(firstName, lastName);
  const promise2 = uploadPhoto(fileName);
  return Promise.allSettled([promise1, promise2]).then((results) => results.map((result) => {
    const newObject = {
      status: result.status,
    };
    if (result.status === 'fulfilled') {
      newObject.value = result.value;
    } else {
      newObject.value = result.reason.toString();
    }
    return newObject;
  }));
}
